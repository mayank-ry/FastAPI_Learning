# FastAPI Learning Path — Todo App

This repo is part of my FastAPI learning journey.
I recently started learning FastAPI and this is my first small project — a **Todo App** built using:

* **FastAPI**
* **Pydantic**
* **Python**
* Basic API routes (GET, POST, PUT, DELETE)

---

## 🚀 Project Overview

This Todo App is a simple backend project where you can:

* Add tasks
* View all tasks
* View a task by ID
* Update a task
* Delete a task

It helped me understand:

* How FastAPI works
* How to create routes
* How Pydantic models work
* API structure in Python

---

## 📁 Folder Structure

```
project/
│── main.py
│── models.py
│── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Create virtual env
2. Install dependencies

   ```
   pip install -r requirements.txt
   ```
3. Run the server

   ```
   uvicorn main:app --reload
   ```
4. Open docs in browser:
   `http://127.0.0.1:8000/docs`

---

## 📝 Learning Goal

Build small apps → understand core FastAPI features → move to DB integration → authentication → full backend apps.

---

## ⭐ Future Improvements

* Add database (SQLite / PostgreSQL)
* Add authentication
* Add frontend

---

## 🙌 Thanks

This is just the beginning of my FastAPI journey. More projects coming soon!
