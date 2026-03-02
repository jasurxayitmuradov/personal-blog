
---

# 📝 Django Personal Blog Project

Welcome! This is a starter project designed to teach the fundamentals of the **Django Web Framework**. By building this blog, you will master the **CRUD** (Create, Read, Update, Delete) cycle.

## 🚀 Learning Objectives

* Understand **MVT** (Model-View-Template) architecture.
* Work with **Databases** and Migrations.
* Handle **Forms** and User inputs (POST/GET).
* Implement **Authentication** to secure the Admin Dashboard.

---

## 🛠 Setup Instructions

1. **Create Virtual Environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows

```


2. **Install Django:**
```bash
pip install django

```


3. **Database Setup:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate

```


4. **Create Admin Account:**
```bash
python3 manage.py createsuperuser

```


5. **Run Server:**
```bash
python3 manage.py runserver

```



---

## 📁 Project Structure

* **Guest Section:**
* `Home`: List of all articles.
* `Article Detail`: Full view of a single post.


* **Admin Section (Protected):**
* `Dashboard`: Manage posts (View, Edit, Delete).
* `Add/Edit`: Custom forms to create and update content.



---

## 💡 Practice Challenge for Students

To take this project to the next level:

1. **Style it:** Use CSS to match the original mockups.
2. **Categories:** Add a Category field to the Article model.
3. **Search:** Implement a search bar to filter articles by title.

**Happy Coding!** 💻✨

---

