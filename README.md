# Task_Manager
# Django Task Manager

## 🚀 Features
- Create and assign tasks.
- View all tasks or user-specific tasks.

## 📂 Setup
```bash
git clone <repo-url>
cd task_manager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Follow prompts
python manage.py runserver
```
Visit `http://127.0.0.1:8000/tasks/`