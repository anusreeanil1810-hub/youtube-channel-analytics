# YouTube Channel Analytics System

## Mini Project

### Developed By

**Anusree Anil**  
B.Tech Computer Science and Engineering

---

# Project Overview

The YouTube Channel Analytics System is a web application developed using **Python, Flask, HTML, CSS, JavaScript, and ShaktiDB**. The application allows users to create an account, log in securely, search for YouTube channels stored in the database, and view channel information such as subscribers, views, uploaded videos, analytics charts, and search history.

The main objective of this project is to understand web application development using Flask and database management using ShaktiDB.

---

# Features

- User Registration
- User Login
- Session Management
- Search YouTube Channels
- View Channel Details
- Display Subscribers
- Display Total Views
- Display Number of Videos
- Display Country Information
- View Recent Uploaded Videos
- Analytics Charts
- Search History
- Logout
- Error Messages for Invalid Login and Invalid Channel Search

---

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Chart.js
- ShaktiDB
- Psycopg2
- Git
- GitHub

---

# Database Tables

| Table Name | Description |
|------------|-------------|
| users | Stores user registration and login details |
| channels | Stores YouTube channel information |
| videos | Stores uploaded video details |
| analytics | Stores subscriber and view analytics |
| search_history | Stores channel search history |

---

# Project Structure

```
youtube-channel-analytics/

│── app.py
│── db.py
│── database.sql
│── test_db.py
│── requirements.txt
│── README.md
│
├── static
│   └── css
│       ├── style.css
│       └── dashboard.css
│
├── templates
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│   ├── dashboard.html
│   └── history.html
│
└── screenshots
```

---

# How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-link>
```

### 2. Open the Project Folder

```bash
cd youtube-channel-analytics
```

### 3. Activate the Virtual Environment

**Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Start the ShaktiDB Server

Make sure the ShaktiDB server is running before starting the application.

### 6. Import the Database

Import the `database.sql` file into the `youtube_project` database.

### 7. Run the Application

```bash
python3 app.py
```

### 8. Open the Application

Visit the following URL in your browser:

```
http://127.0.0.1:5000
```

---

# Working of the Project

1. The user creates a new account using the Sign Up page.
2. The user logs in using registered credentials.
3. After successful login, the Home page is displayed.
4. The user searches for a YouTube channel.
5. The application retrieves the channel information from the ShaktiDB database.
6. The dashboard displays:
   - Channel Details
   - Subscribers
   - Views
   - Number of Videos
   - Recent Videos
   - Analytics Charts
7. Every search is stored in the Search History table.
8. Invalid login credentials or unavailable channels display appropriate error messages.

---

# Screenshots

Add screenshots of the following pages:

- Login Page
- Sign Up Page
- Home Page
- Dashboard
- Search History

---

# Future Improvements

- Connect with the YouTube Data API to fetch live data.
- Add user profile management.
- Export analytics reports as PDF.
- Improve dashboard with additional analytics.
- Add advanced search and filtering.
- Improve chart visualizations.

---

# Learning Outcomes

This project helped in understanding:

- Flask Web Development
- Database Connectivity using Psycopg2
- ShaktiDB Database Management
- SQL Queries
- HTML, CSS and JavaScript
- CRUD Operations
- User Authentication
- Session Management
- Data Visualization using Chart.js

---

# Conclusion

The YouTube Channel Analytics System is a simple database-driven web application that demonstrates the integration of Flask with ShaktiDB. It provides user authentication, channel search, analytics visualization, and search history management. The project helped in gaining practical experience in backend development, frontend design, and database integration.

---

# Author

**Anusree Anil**

B.Tech Computer Science and Engineering

---

## License

This project was developed for educational and academic purposes.
