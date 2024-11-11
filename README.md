# Django To-Do List README

#

## Overview

This repository contains a Django web application for managing a To-Do List. This README provides instructions on how to set up and run the Django development server for testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package installer)
- Django (version 3.x or higher)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/todolist.git
   cd todolist
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Development Server

1. **Apply migrations:**

   Make sure to apply any database migrations:

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**

   If you need access to the Django admin, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

4. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to view your To-Do List application.

   If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/`.

## Features

- Add, edit, and delete tasks
- Mark tasks as completed
- Filter tasks by status (completed/incomplete)
- User authentication for managing personal task lists

## Stopping the Server

To stop the server, press `Ctrl + C` in the terminal where the server is running.

## Additional Notes

- Make sure to check the `settings.py` file for any specific configurations related to your application.
- For testing purposes, you can use the built-in Django test client or any other testing framework you prefer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README further to suit your specific project needs!
