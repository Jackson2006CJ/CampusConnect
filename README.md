
CampusConnect
Student Resource Management and AI Support System
CampusConnect is a student resource management system designed to centralize academic information, assignment tracking, campus communication, student-support services, and campus resources within one application.

The project is being developed in phases. The completed first phase is a working C++ customer-support prototype. The planned final product will expand the prototype into a Flask and MySQL web application with secure accounts, role-based dashboards, academic tools, AI-assisted support, ticket management, and staff analytics.

Project Goals
CampusConnect is designed to:

Centralize student and campus-support information
Help students manage courses, assignments, notes, and deadlines
Improve communication among students, advisors, and support sta
Provide access to campus resources and announcements
Answer common campus-support questions
Create support tickets for questions requiring human assistance
Provide analytics that help staff identify common support needs
Primary Users
Students
Students will be able to view courses, assignments, deadlines, messages, notifications, and campus resources. Students will also be able to add notes and ask the support assistant questions.

Advisors
Advisors will be able to review student progress, send messages, publish reminders, and direct students to appropriate resources.

Support Staff
Support staff will be able to publish campus updates, manage resources, review support tickets, update ticket statuses, and view support analytics.

Current Prototype
The current prototype was developed in C++ using CLion and CMake.

Completed Features
Accept multiple questions during one session
Answer common financial-aid questions
Answer admissions questions
Answer registration questions
Answer tutoring questions
Answer login and password questions
Recognize selected spelling mistakes
Provide a fallback response for unanswered questions
Collect the customer’s name
Generate numbered support tickets
Save support tickets in a text file
Store ticket questions and statuses
Allow staff to view saved tickets
Allow users to exit the program
Track development through Git and GitHub
The current prototype uses rule-based keyword matching. It demonstrates the support and ticket workflow, but it is not yet the final AI-integrated application.

Example Interaction
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


Technology Stack
Current Prototype

C++
CLion
CMake
Git
GitHub
Text-file ticket storage

Planned Web Application

Python
Flask
HTML
CSS
JavaScript
MySQL
Responsive web design
Role-based authorization
AI-assisted campus support
Support-ticket analytics


Development Roadmap

Phase 1: C++ Prototype

Build the customer-support prototype
Add multiple-question support
Add selected typo recognition
Add ticket creation
Add ticket file storage
Add staff ticket viewing
Push the prototype to GitHub


Phase 2: Flask Web Foundation

Create the Flask project structure
Build the CampusConnect homepage
Add shared navigation and styling
Create registration and login pages
Add password hashing
Add role-based authorization


Phase 3: MySQL Integration

Create the MySQL database
Connect Flask to MySQL
Store users and roles
Store courses and assignments
Store notes and messages
Move support tickets from text files to MySQL


Phase 4: Role-Based Dashboards

Build the Student dashboard
Build the Advisor dashboard
Build the Support Staff dashboard
Add campus-resource management
Add messages and notifications


Phase 5: AI Support and Analytics

Build the web-based support assistant
Connect the assistant to approved campus information
Add confidence-based ticket escalation
Add ticket-status management
Add staff analytics


Phase 6: Testing and Presentation

Test all user roles
Test access restrictions
Test database operations
Test mobile and desktop layouts
Update the UML diagrams
Create the final presentation
Prepare the live demonstration


Documentation
Detailed documentation will be stored separately:

docs/PROJECT_WRITEUP.md
docs/REQUIREMENTS.md
docs/PRODUCT_BACKLOG.md
docs/UML_DESIGN.md
These files will contain the complete project write-up, functional and non-functional requirements, user stories, and corrected UML documentation.

Current Limitations
The current prototype:

Runs in a command-line interface
Uses rule-based keyword matching
Stores tickets in a local text file
Does not currently include account authentication
Does not currently use MySQL
Does not currently provide browser-based dashboards
Does not currently connect to an external AI service
These limitations will be addressed in later development phases.

Privacy and Security
The repository must not contain:

Real student records
Real passwords
API keys
Database passwords
Private support conversations
Personally identifiable education records
Only source code, documentation, UML diagrams, and safe sample data should be uploaded.

Project Vision
The completed CampusConnect system will provide students, advisors, and support staff with one secure and organized environment for academic planning, communication, campus-resource access, and student support.

The C++ prototype demonstrates the initial support-ticket workflow. The final Flask and MySQL system will expand that work into a responsive web application with role-based dashboards, database storage, AI-assisted support, and staff analytics.  Database passwords
Private support conversations
Personally identifiable education records
Only source code, documentation, UML diagrams, and safe sample data should be uploaded.

Project Vision
The completed CampusConnect system will provide students, advisors, and support staff with one secure and organized environment for academic planning, communication, campus-resource access, and student support.

The C++ prototype demonstrates the initial support-ticket workflow. The final Flask and MySQL system will expand that work into a responsive web application with role-based dashboards, database storage, AI-assisted support, and staff analytics.
