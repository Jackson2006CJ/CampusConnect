# CampusConnect
Student Resource Management and AI Support System
CampusConnect is a centralized student resource management system designed to bring academic information, assignment tracking, campus communication, student support, and campus resources into one application.

The purpose of CampusConnect is to reduce the need for students to switch between multiple disconnected platforms. Students, advisors, and campus support staff will use role-based dashboards to access the information and tools relevant to them.

CampusConnect is currently under active development. The completed first phase is a C++ customer-support prototype that demonstrates question handling, support-ticket creation, file storage, and staff ticket viewing. The long-term system will expand this prototype into a database-backed Flask web application with user accounts, role-based dashboards, academic tools, AI-assisted support, and data analytics.

Project Problem
Students often access course information, assignments, deadlines, messages, announcements, and campus resources through separate systems. This fragmentation can make important information difficult to locate and increases the possibility of missed deadlines or campus updates.

CampusConnect addresses this problem by creating one structured system where users can access academic information, communicate with campus personnel, locate support resources, and request assistance.

Project Objectives
CampusConnect is designed to:

Centralize academic and campus-support information
Provide personalized dashboards based on user roles
Help students track courses, assignments, notes, and deadlines
Improve communication between students, advisors, and support staff
Provide access to tutoring, advising, financial aid, and other resources
Answer common campus-support questions
Escalate unanswered questions into support tickets
Help support staff identify common questions and service needs
Store user and academic information securely in a relational database
Provide a responsive interface for desktop and mobile browsers
Primary Users
Students
Students will be able to:

Create an account and log in
Access a personalized dashboard
View courses and assignments
Review upcoming deadlines
Add personal notes
Receive notifications and announcements
Send and receive messages
View campus resources
Ask the CampusAssist support assistant questions
Create support tickets when additional help is needed
Advisors
Advisors will be able to:

Log in through a role-protected account
View assigned students
Review student progress
Post assignment reminders
Send guidance messages
Publish announcements
Direct students to appropriate campus resources
Support Staff
Support staff will be able to:

Publish campus alerts and updates
Add and update campus resources
View student support tickets
Update ticket statuses
Review frequently asked questions
View support analytics
Maintain approved information used by the support assistant
Current Development Status
Phase 1: C++ Customer-Support Prototype
The first working prototype was developed in C++ using CLion and CMake.

The current prototype can:

Accept multiple questions during one session
Convert input to lowercase for consistent keyword matching
Answer common questions about:
Financial aid
Admissions
Login and password assistance
Course registration
Tutoring
Recognize selected financial-aid spelling mistakes
Provide a fallback response for unsupported questions
Ask for the customer’s name
Generate numbered support tickets
Save tickets in support_tickets.txt
Store each ticket’s customer, question, and status
Allow staff to enter the staff command to view tickets
Allow users to enter the exit command to end the program
Preserve source-code versions through Git and GitHub
The current prototype uses rule-based keyword matching. It demonstrates the planned support workflow, but it is not yet the final AI-integrated web application.

Example Prototype Interaction
====================================
        CampusAssist AI
 School Customer Support Prototype
====================================
Ask a question, type 'staff' to view tickets, or type 'exit' to quit.

You: Where can I get a parking permit?

CampusAssist: I could not confidently answer that question.
Your request will be forwarded to a school support representative.

CampusAssist: Please enter your name: CJ
CampusAssist: Support ticket #1001 was created successfully.

You: staff

====================================
        OPEN SUPPORT TICKETS
====================================
Ticket ID: 1001
Customer: CJ
Question: Where can I get a parking permit?
Status: Open
------------------------------------

You: exit

CampusAssist: Thank you for using CampusAssist AI. Goodbye!
