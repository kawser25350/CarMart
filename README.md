# CarMart - Django Web Application

## Overview
A beginner-friendly, class-based Django project that demonstrates a full-stack web application for a car rental/sales platform. Built as part of academic coursework to showcase understanding of Django fundamentals and front-end integration.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage Walkthrough](#usage-walkthrough)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)

## Tech Stack
- **Backend**: Python 3.13.9, Django 6.0.5 (Class-Based Views)
- **Database**: SQLite (default) / PostgreSQL (configurable)
- **Frontend**: HTML5, CSS3, Bootstrap 5, vanilla JavaScript
- **Styling**: Custom CSS with responsive design
- **Deployment**: Ready for Heroku/Render deployment

## Features
- User authentication (login, registration, profile)
- Car listing with detailed specifications
- Search and filter functionality
- Shopping cart / inquiry system
- Admin dashboard for managing cars and orders
- Responsive UI for desktop and mobile devices

## Project Structure
```
car_mart/
├── car/                 # Core car application
│   ├── models.py        # Django models (Car, Order, etc.)
│   ├── views.py         # Class-based views (ListView, DetailView, CreateView)
│   ├── urls.py          # URL routing
│   └── templates/       # HTML templates
├── accounts/            # User account functionality
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── brand/               # Optional brand management
├── orders/              # Order management
├── car_mart/            # Project settings
│   ├── settings.py
│   └── urls.py
└── static/              # CSS, JS, images
    └── css/
    └── js/
    └── images/
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CarMart.git
   cd CarMart
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Project
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000` in your browser.

## Usage Walkthrough
- **Home Page**: Showcases featured cars with image carousel
- **Car Details**: Displays specifications, price, and inquiry form
- **User Registration**: Secure signup/login with email verification (basic)
- **Admin Panel**: Manage inventory, view orders, and user accounts

## Learning Outcomes
- Mastery of Django class-based views (ListView, DetailView, CreateView, UpdateView)
- Understanding of Django URL routing and template inheritance
- Implementation of basic authentication and authorization
- Integration of front-end UI with Django templates
- Database modeling with relationships (ForeignKey, ManyToManyField)
- Deployment preparation and environment configuration

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



