1. Customer Statement of Requirements
   
CampusConnect is a centralized student resource management system designed to unify academic information, assignment tracking, and campus communication into a single web application. The purpose of the system is to reduce fragmentation across multiple platforms and ensure students, advisors, and campus personnel have continuous 
access to essential academic tools. CampusConnect provides personalized dashboards, course information, assignment deadlines, advisor messages, and campus announcements through a secure, database‑backed interface. The system supports multiple user roles and maintains reliable access to academic resources throughout the student lifecycle.

2. Requirements Specification
   
    Functional Requirements

    User Accounts and Authentication
The system must allow users to create accounts.
The system must authenticate users using a secure login mechanism.
The system must assign roles such as Student, Advisor, or Support Staff.

    Dashboard
The system must display a personalized dashboard after login.
Students must be able to view courses, assignments, deadlines, and notes.
Advisors must be able to view student progress and send announcements.
Support staff must be able to publish campus updates and resources.

    Course and Assignment Management
Students must be able to view course lists and assignment schedules.
Students must be able to add personal notes to assignments or courses.
Advisors must be able to post assignment reminders or updates.

    Communication Tools
Advisors must be able to send messages to students.
Students must be able to receive notifications and announcements.
Support staff must be able to publish campus‑wide alerts.

    Resource Management
The system must store campus resources such as tutoring, advising, and support services.
Users must be able to access resource descriptions and availability.

    Database Interaction
The system must retrieve user‑specific data from the database.
The system must update database entries when users modify notes or settings.
The system must enforce role‑based access control for all data operations.

     Non‑Functional Requirements
   
   Performance
The system must load dashboard content within two seconds.
Database queries must execute efficiently under typical student load.

    Security
User passwords must be encrypted.
Role‑based access must prevent unauthorized data access.
All communication must occur over HTTPS.

    Reliability
The system must maintain persistent database connections.
The system must handle unexpected failures gracefully.

    Usability
The interface must be simple and intuitive for all user roles.
Navigation must follow a predictable layout to reduce cognitive load.

    Scalability
The system must support increasing numbers of students and advisors.
The database must scale to store multiple semesters of academic data.

   Compatibility
The system must run on modern browsers such as Chrome, Firefox, and Edge.
The interface must render consistently across desktop and mobile devices.

    3. Data and Storage Blueprint
  
    Data Input
CampusConnect will accept data through the following mechanisms:

    Manual Entry  
Students enter notes, update personal deadlines, and manage assignment details.
Advisors enter announcements, reminders, and guidance messages.
Support staff enter campus updates and resource information.

   Automated Retrieval  
The system retrieves course lists, assignments, and user profiles from the database using backend queries.

   Database or Storage Solution
CampusConnect will use a MySQL relational database for structured storage of:

    User accounts
    Course information
    Assignment schedules
    Advisor messages
    Campus resources
    Notes and personal data

MySQL was selected for its reliability, structured schema support, efficient querying, and long‑term scalability. 
The backend will interact with MySQL through Python Flask using secure, parameterized queries.

   4. Agile Product Backlog (User Stories)
    
Below are the user stories you will log as GitHub Issues.

   User Authentication
   
As a student, I want to log into CampusConnect so that I can access my academic dashboard.
As an advisor, I want to log into CampusConnect so that I can view and support my assigned students.
As support staff, I want to log in to CampusConnect so that I can publish campus resources.

   Dashboard

As a student, I want to see my courses and assignments so that I can stay organized.
As a student, I want to view upcoming deadlines so that I can manage my time.
As an advisor, I want to see student progress so that I can provide guidance.
As support staff, I want to publish campus updates so that students stay informed.

   Course and Assignment Tools
   
As a student, I want to add notes to my assignments so that I can track important details.
As an advisor, I want to post assignment reminders so that students stay on track.
   
   Communication
   
As an advisor, I want to send messages to students so that I can communicate important information.
As a student, I want to receive notifications so that I do not miss deadlines or announcements.

   Resource Management
   
As a student, I want to view campus resources so that I can access support services.
As support staff, I want to update resource information so that students have accurate details.

   Database Interaction
   
As a user, I want my dashboard to load personalized data so that I see information relevant to me.
As a user, I want my changes saved to the database so that my information stays updated.




