# Employee Management System (EMS) 🏢

A full-featured web application built with **Django** to manage company workforce records, departments, employee profiles, and organizational data. This project was developed as a capstone project following the completion of **Django Training** during college.

---

> [!NOTE]
> **Project Attribution & Development Note:**  
> The **backend architecture, database schemas, business logic, routing, CRUD views, and model relationships** were independently authored and implemented by me, following hands-on Django college training.  
> The **frontend UI & layout styling** were created with the assistance of **AI** to streamline development time and deliver a modern, polished visual presentation.

---

## 🌟 Key Features

- **Employee CRUD Operations**:
  - **Create**: Add new employees with detailed fields including name, email, salary, experience, designation, city, address, employment status, department selection, and profile picture upload.
  - **Read / Directory**: Responsive directory table and cards displaying employee summaries, contact info, and current work status.
  - **Update**: Edit existing employee profiles, modify information, and replace profile pictures seamlessly.
  - **Delete**: Safely delete employee records from the database with confirmation redirection.
- **Detailed Employee Profile View**:
  - Dedicated employee profile page (`/employee/<id>/`) showcasing all professional and personal details alongside the uploaded photo.
- **Relational Data Modeling**:
  - Department model linked to Employees via ForeignKey (`on_delete=models.CASCADE`, `related_name='Employess'`).
- **Dynamic Media Handling**:
  - File/image upload support configured via Django's `MEDIA_URL` and `MEDIA_ROOT` with `Pillow`.
- **Django Admin Dashboard**:
  - Pre-configured admin interface with search fields, list filters, and custom ordering for quick internal management.
- **Informational Pages**:
  - Interactive Landing/Home page, About page, and Contact page.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Backend Framework** | Python 3, Django (MVT Architecture) |
| **Database** | SQLite3 (Default for local development; swappable with PostgreSQL/MySQL) |
| **Image Processing** | Pillow |
| **Frontend / UI** | HTML5, CSS3, Bootstrap 5, Bootstrap Icons, Google Fonts (Inter) *(AI-assisted design)* |
| **WSGI / Production Server** | Gunicorn, WhiteNoise |

---

## 📁 Project Directory Structure

```text
Employee/
├── App1/                      # General navigation & informational views
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py                # Home, About, Contact routing
│   └── views.py
├── App2/                      # Core business logic: Employee & Department management
│   ├── migrations/
│   ├── admin.py               # Customized ModelAdmin registrations
│   ├── apps.py
│   ├── models.py              # Employee and Department database models
│   ├── urls.py                # CRUD endpoints & detail views
│   └── views.py               # Add, edit, delete, list, and detail views
├── Employee/                  # Main project configuration
│   ├── asgi.py
│   ├── settings.py            # Installed apps, middleware, media & template paths
│   ├── urls.py                # Root URL dispatcher
│   └── wsgi.py
├── Templates/                 # HTML templates
│   ├── base.html              # Base layout with navbar, footer, and styling
│   ├── home.html              # Landing page
│   ├── empdata.html           # Employee directory / records list
│   ├── form.html              # Add new employee form
│   ├── editform.html          # Update employee details form
│   ├── employee_details.html  # Comprehensive single employee profile
│   ├── about.html             # About page
│   └── contact.html           # Contact page
├── media/                     # Uploaded employee profile pictures
│   └── employees/
├── static/                    # Custom static assets (CSS, JS, images)
├── manage.py                  # Django CLI runner
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files excluded from git & deployment
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started (Local Setup)

### 1. Prerequisites
- Python 3.10+ installed on your system.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd Employee
```

### 3. Create and Activate a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompt to set your username, email, and password.

### 7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
- **Application Homepage**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Employee Directory**: [http://127.0.0.1:8000/empdata/](http://127.0.0.1:8000/empdata/)
- **Add Employee**: [http://127.0.0.1:8000/form/](http://127.0.0.1:8000/form/)
- **Django Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🚢 Deployment Guide

When deploying this project to production platforms (such as **Render**, **Railway**, **PythonAnywhere**, or an **Ubuntu VPS**), keep the following points in mind:

### 1. Environment Configuration (`Employee/settings.py`)
- **SECRET_KEY**: Store the Django secret key in an environment variable instead of hardcoding it.
- **DEBUG**: Set `DEBUG = False` in production.
- **ALLOWED_HOSTS**: Add your live domain or hosting URL (e.g., `ALLOWED_HOSTS = ['your-app.onrender.com', 'localhost', '127.0.0.1']`).

### 2. Static and Media File Handling
- In production, static files can be served using [WhiteNoise](http://whitenoise.evans.io/en/stable/).
- Because user-uploaded media files (employee profile pictures) in `media/` are ephemeral on cloud hosts like Render or Heroku, consider connecting a cloud storage service like **Cloudinary** or **AWS S3** for persistent image storage in production.

### 3. Start Command (WSGI)
For cloud platforms using a Procfile or custom start command:
```bash
gunicorn Employee.wsgi:application
```

---

## 👨‍💻 Author

- Developed by **Piyush** following College Django Training.
- UI Design: Designed with the assistance of AI to speed up frontend development.
- Backend & Architecture: Custom built with Django & Python.
