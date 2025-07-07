# Pylearner
# PyLearner 🧠

PyLearner is a Django-based learning platform for Python concepts and projects.

## 🔧 Features

- Admin-only post creation
- Posts sorted by date
- HTML/CSS/JS frontend
- Mobile responsive

## 🚀 Live Site

[https://pylearner.onrender.com](https://pylearner.onrender.com) *(replace with actual URL after deployment)*

## 🛠️ Tech Stack

- Python 3.11+
- Django 5.2.3
- HTML, CSS, JavaScript
- Gunicorn, WhiteNoise (for hosting)

## 🧩 Setup Instructions

```bash
git clone https://github.com/your-username/pylearner.git
cd pylearner
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

├── myproject/
│   ├── settings.py
│   └── wsgi.py
├── posts/
├── users/
├── static/
├── templates/
├── requirements.txt
├── Procfile
└── manage.py
