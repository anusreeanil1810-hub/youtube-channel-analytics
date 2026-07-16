# YouTube Channel Analytics System

## Mini Project

### Developed By

**Anusree Anil**  
B.Tech Computer Science and Engineering

---

## Project Overview

The YouTube Channel Analytics System is a web application developed using **Python, Flask, HTML, CSS, JavaScript, Chart.js, and ShaktiDB**. The application allows users to register, log in, search for YouTube channels stored in the database, and view channel information through an analytics dashboard.

---

## Features

- User Registration
- User Login
- User Logout
- Search YouTube Channels
- View Channel Details
- Display Subscriber Count
- Display Total Views
- Display Number of Videos
- Display Country Information
- Display Recent Videos
- Display Analytics Charts
- Store Search History
- Display Error Messages for Invalid Login and Invalid Channel Search

---

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Chart.js
- ShaktiDB
- Psycopg2

---

## Database Tables

- **users** – Stores user registration and login details.
- **channels** – Stores YouTube channel information.
- **videos** – Stores video details for each channel.
- **analytics** – Stores subscriber and view analytics.
- **search_history** – Stores the user's search history.

---

## Project Structure

```text
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
```

---

## How to Run the Project

1. Clone the repository.

```bash
git clone <repository-link>
```

2. Open the project folder.

```bash
cd youtube-channel-analytics
```

3. Activate the virtual environment.

**Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

4. Install the required packages.

```bash
pip install -r requirements.txt
```

5. Start the ShaktiDB server.

6. Import the `database.sql` file into the `youtube_project` database.

7. Run the application.

```bash
python3 app.py
```

8. Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Working

1. The user creates a new account using the Sign Up page.
2. The user logs in using registered credentials.
3. After successful login, the Home page is displayed.
4. The user searches for a YouTube channel.
5. The application retrieves channel information from the ShaktiDB database.
6. The dashboard displays channel details, analytics charts, and recent videos.
7. Every search is stored in the search history.
8. Invalid login credentials or unavailable channels display appropriate error messages.

---

## Conclusion

The YouTube Channel Analytics System is a database-driven web application that demonstrates the integration of Flask with ShaktiDB. It provides user authentication, channel search, analytics visualization, and search history management. This project helped in understanding database connectivity, SQL queries, frontend development, and backend integration.

---

## Author

**Anusree Anil**  
B.Tech Computer Science and Engineering
