# Django-Projectus
# Django Projectus: Beginner's Guide

Welcome to the **Django Projectus** repository! This beginner-friendly project includes a **Todo List**, a **CRUD application**, a **Weather App**, and an exciting **Currency Graph Predictor**. Whether you're new to Django or just looking to explore, this guide will help you set up and run the project.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up the Project](#setting-up-the-project)
3. [Todo List](#todo-list)
4. [CRUD Application](#crud-application)
5. [Weather App](#weather-app)
6. [Currency Graph Predictor](#currency-graph-predictor)

## Prerequisites
Before diving into the project, the following should be there:
- **Python** installed (preferably Python 3)
- Basic knowledge of **HTML**, **CSS**, and **JavaScript** (optional but recommended)
- **Django** installed (see installation instructions in the next section)

## Setting Up the Project
1. Clone this repository:
   ```
   git clone https://github.com/your-username/django-projectus.git
   cd django-projectus
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Django and other dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

Now let's explore the different components of the project:

## Todo List
The **Todo List** app allows you to manage your tasks. You can add, edit, and delete tasks. Access it at `http://localhost:8000/todo/`.

## CRUD Application
The **CRUD application** demonstrates basic Create, Read, Update, and Delete operations. It uses a model called `Task` with fields like `title`, `description`, and `completed`. Explore it at `http://localhost:8000/crud/`.

## Weather App
The **Weather App** fetches real-time weather data for various cities using the OpenWeatherMap API. You can search for city weather by name. Access it at `http://localhost:8000/weather/`.

## Currency Graph Predictor
The **Currency Graph Predictor** uses LSTM (Long Short-Term Memory) to predict future currency values. It currently supports Tanzanian Shilling (TZS) and US Dollar (USD). The left graph shows real-time stock prices, while the right graph predicts future prices.

## Deployment (Optional)
To deploy your project, consider using platforms like **Heroku** or **PythonAnywhere**. Refer to their documentation for deployment instructions.



---



