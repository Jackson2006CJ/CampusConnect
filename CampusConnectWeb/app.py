import os
from functools import wraps
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIRECTORY = Path(__file__).resolve().parent
ENV_FILE = BASE_DIRECTORY / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "campusconnect-development-key")


def get_database_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        use_pure=True,
    )


def login_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in to continue.")
            return redirect(url_for("login"))
        return view_function(*args, **kwargs)

    return wrapped_view


def role_required(*allowed_roles):
    def decorator(view_function):
        @wraps(view_function)
        def wrapped_view(*args, **kwargs):
            if not session.get("user_id"):
                flash("Please log in to continue.")
                return redirect(url_for("login"))

            if session.get("role") not in allowed_roles:
                flash("You do not have permission to view that page.")
                return redirect(url_for("dashboard"))

            return view_function(*args, **kwargs)

        return wrapped_view

    return decorator


def support_answer(question):
    normalized = question.lower()

    response_groups = [
        (
            [
                "financial aid",
                "finaal aid",
                "finaial aid",
                "finail aid",
                "finacial aid",
                "fafsa",
            ],
            "For financial aid assistance, contact the Financial Aid Office.",
        ),
        (
            ["admission", "admissions", "application"],
            "For admissions assistance, contact the Admissions Office.",
        ),
        (
            ["registration", "register", "registrar"],
            "For course registration assistance, contact the Registrar Office.",
        ),
        (
            ["tutoring", "tutor", "academic support"],
            "Tutoring is available through the Academic Tutoring Center.",
        ),
        (
            ["password", "login", "account access"],
            "For login or password assistance, contact the IT Help Desk.",
        ),
    ]

    for keywords, answer in response_groups:
        if any(keyword in normalized for keyword in keywords):
            return answer

    return None


def ticket_category(question):
    normalized = question.lower()

    if any(word in normalized for word in ["financial aid", "fafsa", "tuition"]):
        return "Financial Aid"
    if any(word in normalized for word in ["admission", "application", "apply"]):
        return "Admissions"
    if any(word in normalized for word in ["registration", "register", "course"]):
        return "Registration"
    if any(word in normalized for word in ["tutoring", "tutor", "academic support"]):
        return "Tutoring"
    if any(word in normalized for word in ["password", "login", "technology"]):
        return "Technology"

    return "General Support"


@app.route("/")
def home():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM resources ORDER BY title")
    resources = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template("home.html", resources=resources)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        role = request.form["role"]
        allowed_roles = {"Student", "Advisor", "Support Staff"}

        if role not in allowed_roles:
            flash("Please select a valid role.")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must contain at least eight characters.")
            return redirect(url_for("register"))

        connection = get_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (full_name, email, password_hash, role)
                VALUES (%s, %s, %s, %s)
                """,
                (full_name, email, generate_password_hash(password), role),
            )
            connection.commit()
            flash("Account created successfully. Please log in.")
            return redirect(url_for("login"))
        except mysql.connector.IntegrityError:
            flash("An account with that email already exists.")
            return redirect(url_for("register"))
        finally:
            cursor.close()
            connection.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["user_id"]
            session["full_name"] = user["full_name"]
            session["role"] = user["role"]
            flash(f"Welcome, {user['full_name']}! You are logged in as {user['role']}.")
            return redirect(url_for("dashboard"))

        flash("Incorrect email or password.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/dashboard")
@login_required
def dashboard():
    role = session.get("role")

    if role == "Student":
        return redirect(url_for("student_dashboard"))
    if role == "Advisor":
        return redirect(url_for("advisor_dashboard"))
    if role == "Support Staff":
        return redirect(url_for("staff_dashboard"))

    flash("Your account role is not recognized.")
    return redirect(url_for("home"))


@app.route("/student")
@role_required("Student")
def student_dashboard():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM courses ORDER BY course_code")
    courses = cursor.fetchall()

    cursor.execute(
        """
        SELECT assignments.*, courses.course_code
        FROM assignments
                 JOIN courses ON assignments.course_id = courses.course_id
        ORDER BY assignments.due_date
        """
    )
    assignments = cursor.fetchall()

    cursor.execute("SELECT * FROM announcements ORDER BY created_at DESC LIMIT 10")
    announcements = cursor.fetchall()

    cursor.execute("SELECT * FROM resources ORDER BY title")
    resources = cursor.fetchall()

    cursor.execute(
        """
        SELECT * FROM support_tickets
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (session["user_id"],),
    )
    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "student_dashboard.html",
        courses=courses,
        assignments=assignments,
        announcements=announcements,
        resources=resources,
        tickets=tickets,
    )


@app.route("/advisor", methods=["GET", "POST"])
@role_required("Advisor")
def advisor_dashboard():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        title = request.form["title"].strip()
        message = request.form["message"].strip()
        cursor.execute(
            """
            INSERT INTO announcements (author_id, title, message)
            VALUES (%s, %s, %s)
            """,
            (session["user_id"], title, message),
        )
        connection.commit()
        cursor.close()
        connection.close()
        flash("Announcement published successfully.")
        return redirect(url_for("advisor_dashboard"))

    cursor.execute(
        """
        SELECT user_id, full_name, email, role
        FROM users
        WHERE role = 'Student'
        ORDER BY full_name
        """
    )
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM courses ORDER BY course_code")
    courses = cursor.fetchall()

    cursor.execute("SELECT * FROM announcements ORDER BY created_at DESC LIMIT 10")
    announcements = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "advisor_dashboard.html",
        students=students,
        courses=courses,
        announcements=announcements,
    )


@app.route("/staff", methods=["GET", "POST"])
@role_required("Support Staff")
def staff_dashboard():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "resource":
            cursor.execute(
                """
                INSERT INTO resources
                    (title, category, description, location, availability)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    request.form["title"].strip(),
                    request.form["category"].strip(),
                    request.form["description"].strip(),
                    request.form["location"].strip(),
                    request.form["availability"].strip(),
                ),
            )
            flash("Campus resource added successfully.")

        elif form_type == "announcement":
            cursor.execute(
                """
                INSERT INTO announcements (author_id, title, message)
                VALUES (%s, %s, %s)
                """,
                (
                    session["user_id"],
                    request.form["title"].strip(),
                    request.form["message"].strip(),
                ),
            )
            flash("Campus update published successfully.")

        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for("staff_dashboard"))

    cursor.execute("SELECT * FROM support_tickets ORDER BY created_at DESC")
    tickets = cursor.fetchall()

    cursor.execute(
        """
        SELECT
            COUNT(*) AS total_tickets,
            SUM(status = 'NEW') AS new_tickets,
            SUM(status = 'IN_PROGRESS') AS in_progress,
            SUM(status = 'RESOLVED') AS resolved
        FROM support_tickets
        """
    )
    analytics = cursor.fetchone()

    for key in ["total_tickets", "new_tickets", "in_progress", "resolved"]:
        analytics[key] = analytics[key] or 0

    cursor.execute(
        """
        SELECT category, COUNT(*) AS ticket_count
        FROM support_tickets
        GROUP BY category
        ORDER BY ticket_count DESC, category
        """
    )
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM resources ORDER BY title")
    resources = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "staff_dashboard.html",
        tickets=tickets,
        analytics=analytics,
        categories=categories,
        resources=resources,
    )


@app.route("/ticket/<int:ticket_id>/status", methods=["POST"])
@role_required("Support Staff")
def update_ticket(ticket_id):
    new_status = request.form.get("status")
    allowed_statuses = {"NEW", "IN_PROGRESS", "RESOLVED"}

    if new_status not in allowed_statuses:
        flash("Invalid ticket status.")
        return redirect(url_for("staff_dashboard"))

    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE support_tickets SET status = %s WHERE ticket_id = %s",
        (new_status, ticket_id),
    )
    connection.commit()
    cursor.close()
    connection.close()

    flash(f"Ticket #{ticket_id} was updated to {new_status}.")
    return redirect(url_for("staff_dashboard"))


@app.route("/support", methods=["GET", "POST"])
@login_required
def support():
    answer = None
    ticket = None

    if request.method == "POST":
        question = request.form["question"].strip()
        answer = support_answer(question)

        if answer is None:
            category = ticket_category(question)
            connection = get_database_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                """
                INSERT INTO support_tickets
                    (user_id, customer_name, question, category, status)
                VALUES (%s, %s, %s, %s, 'NEW')
                """,
                (
                    session["user_id"],
                    session["full_name"],
                    question,
                    category,
                ),
            )
            connection.commit()
            ticket_id = cursor.lastrowid
            cursor.execute(
                "SELECT * FROM support_tickets WHERE ticket_id = %s",
                (ticket_id,),
            )
            ticket = cursor.fetchone()
            cursor.close()
            connection.close()

            answer = (
                "I could not confidently answer that question. "
                "A support ticket was created for human assistance."
            )

    return render_template("support.html", answer=answer, ticket=ticket)


@app.route("/database-test")
def database_test():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE()")
    database_name = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return f"CampusConnect successfully connected to MySQL database: {database_name}"


if __name__ == "__main__":
    app.run(debug=True)
