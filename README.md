# 📘 Student Performance Analyzer (Full Stack Project)

## 🚀 Project Overview

The **Student Performance Analyzer** is a full-stack web application that allows users to manage student records and automatically calculate grades based on marks.

It provides full **CRUD operations (Create, Read, Update, Delete)** and demonstrates integration between frontend, backend, and database.

---

## 🧠 Features

* ➕ Add student with name and marks
* 📊 Automatic grade calculation (A, B, C, Fail)
* 📄 View all student records in a table
* ✏️ Update student details
* ❌ Delete student records
* 🔄 Real-time UI updates

---

## 🛠 Tech Stack

### Frontend:

* React.js
* JavaScript
* HTML
* CSS
* Axios

### Backend:

* FastAPI
* Python
* Pydantic
* SQLAlchemy

### Database:

* SQLite

### Tools:

* VS Code
* Git & GitHub
* FastAPI Swagger UI (/docs)

---

## 🏗 Project Architecture

```
React Frontend
      ↓ (Axios API Calls)
FastAPI Backend
      ↓ (SQLAlchemy ORM)
SQLite Database (students.db)
```

---

## 📊 Database Schema

### Table: students

| Field | Type                  |
| ----- | --------------------- |
| id    | Integer (Primary Key) |
| name  | String                |
| marks | Integer               |
| grade | String                |

---

## 🔥 API Endpoints

| Method | Endpoint       | Description      |
| ------ | -------------- | ---------------- |
| POST   | /students      | Add new student  |
| GET    | /students      | Get all students |
| PUT    | /students/{id} | Update student   |
| DELETE | /students/{id} | Delete student   |

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/anjalichilukuri61/student_performance_analyser.git
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

👉 Open backend docs:

```
http://127.0.0.1:8000/docs
```

---

### 3️⃣ Frontend Setup (React)

```bash
cd student-frontend
npm install
npm start
```

👉 Open frontend:

```
http://localhost:3000
```

---

## 🎯 Project Workflow

```
User Input (React)
      ↓
Axios API Call
      ↓
FastAPI Backend
      ↓
SQLite Database
      ↓
Response → UI Update
```

---

## 🚧 Challenges Faced

* CORS error between frontend and backend
* React state management issues
* Backend update logic debugging
* Database integration using SQLAlchemy

---

## 💡 Key Learnings

* Full-stack development workflow
* REST API creation using FastAPI
* Frontend-backend integration
* CRUD operations with database
* Debugging real-world errors

---

## 📌 Future Improvements

* Add authentication system (login/signup)
* Add charts for performance analysis
* Deploy frontend and backend online
* Add search & filter functionality

---

## 👨‍💻 Author

**Anjali Chilukuri**
B.Tech CSE Student

---

## ⭐ If you like this project

Give a ⭐ to the repository and feel free to contribute!

