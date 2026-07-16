# YouTube Channel Analytics System

## Mini Project

### Developed By
**Anusree Anil**

B.Tech Computer Science and Engineering

---

## Project Overview

The YouTube Channel Analytics System is a web application developed using Flask and ShaktiDB (PostgreSQL). It allows users to create an account, log in, search for YouTube channels, and view channel statistics such as subscribers, views, uploaded videos, and analytics.

The project was developed to understand database connectivity, web development, and data visualization using Python.

---

## Features

- User Registration
- User Login
- Search YouTube Channels
- View Channel Details
- Subscriber Count
- Total Views
- Number of Videos
- Country Information
- Recent Videos
- Analytics Charts
- Search History
- Logout Facility

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Chart.js
- ShaktiDB (PostgreSQL)
- Psycopg2

---

## Database Tables

The project uses the following tables:

- users
- channels
- videos
- analytics
- search_history

---

## Project Structure

```
youtube-channel-analytics/

│── app.py
│── db.py
│── database.sql
│── test_db.py
│── requirements.txt
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

## How to Run the Project

### 1. Clone the repository

```
git clone <repository_link>
```

### 2. Open the project folder

```
cd youtube-channel-analytics
```

### 3. Activate the virtual environment

Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

### 4. Install the required packages

```
pip install -r requirements.txt
```

### 5. Start the database server

Start the ShaktiDB/PostgreSQL server.

### 6. Run the application

```
python3 app.py
```

### 7. Open the browser

```
http://127.0.0.1:5000
```

---

## Working

1. The user first creates an account.
2. After successful registration, the user logs in.
3. The home page allows searching for a YouTube channel.
4. The dashboard displays channel information and analytics.
5. Search history is saved in the database.
6. Invalid login or unavailable channels display appropriate messages.

---

## Future Improvements

- Connect with the YouTube Data API for live channel data.
- Add profile pictures for channels.
- Export analytics as PDF.
- Add advanced filtering and sorting.
- Improve charts with more analytics.

---

## Conclusion

This project helped in learning Flask web development, ShaktiDB database management, SQL queries, frontend design, and database connectivity. It also provided practical experience in developing a complete database-driven web application.

---

## Author

**Anusree Anil**

B.Tech Computer Science and Engineering
