CREATE DATABASE IF NOT EXISTS campusconnect;

USE campusconnect;

CREATE TABLE IF NOT EXISTS users (
                                     user_id INT AUTO_INCREMENT PRIMARY KEY,
                                     full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('Student', 'Advisor', 'Support Staff') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS courses (
                                       course_id INT AUTO_INCREMENT PRIMARY KEY,
                                       course_code VARCHAR(20) NOT NULL,
    course_name VARCHAR(150) NOT NULL,
    instructor_name VARCHAR(100),
    semester VARCHAR(50)
    );

CREATE TABLE IF NOT EXISTS enrollments (
                                           enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
                                           user_id INT NOT NULL,
                                           course_id INT NOT NULL,
                                           FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS assignments (
                                           assignment_id INT AUTO_INCREMENT PRIMARY KEY,
                                           course_id INT NOT NULL,
                                           title VARCHAR(150) NOT NULL,
    description TEXT,
    due_date DATETIME,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS notes (
                                     note_id INT AUTO_INCREMENT PRIMARY KEY,
                                     user_id INT NOT NULL,
                                     assignment_id INT,
                                     note_text TEXT NOT NULL,
                                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                     FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE,
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id)
    ON DELETE SET NULL
    );

CREATE TABLE IF NOT EXISTS announcements (
                                             announcement_id INT AUTO_INCREMENT PRIMARY KEY,
                                             author_id INT,
                                             title VARCHAR(150) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(user_id)
    ON DELETE SET NULL
    );

CREATE TABLE IF NOT EXISTS messages (
                                        message_id INT AUTO_INCREMENT PRIMARY KEY,
                                        sender_id INT NOT NULL,
                                        receiver_id INT NOT NULL,
                                        subject VARCHAR(150),
    message_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(user_id)
    ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES users(user_id)
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS resources (
                                         resource_id INT AUTO_INCREMENT PRIMARY KEY,
                                         title VARCHAR(150) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(150),
    availability VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS support_tickets (
                                               ticket_id INT AUTO_INCREMENT PRIMARY KEY,
                                               user_id INT,
                                               customer_name VARCHAR(100) NOT NULL,
    question TEXT NOT NULL,
    category VARCHAR(100) DEFAULT 'General Support',
    status ENUM('NEW', 'IN_PROGRESS', 'RESOLVED') DEFAULT 'NEW',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE SET NULL
    );

INSERT INTO courses
(course_code, course_name, instructor_name, semester)
VALUES
    ('COSC 369', 'Software Engineering I', 'Course Instructor', 'Fall 2026'),
    ('COSC 208', 'Computer Science II', 'Course Instructor', 'Fall 2026');

INSERT INTO resources
(title, category, description, location, availability)
VALUES
    (
        'Academic Tutoring Center',
        'Tutoring',
        'Provides academic tutoring and study assistance.',
        'Academic Support Center',
        'Monday through Friday'
    ),
    (
        'Financial Aid Office',
        'Financial Aid',
        'Assists students with financial aid and FAFSA questions.',
        'Administration Building',
        'Monday through Friday'
    ),
    (
        'Registrar Office',
        'Registration',
        'Assists students with course registration and academic records.',
        'Administration Building',
        'Monday through Friday'
    ),
    (
        'IT Help Desk',
        'Technology',
        'Provides login, password, and account assistance.',
        'Technology Services',
        'Monday through Friday'
    );