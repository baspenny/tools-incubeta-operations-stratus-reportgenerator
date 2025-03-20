# Stratus Report Generator

A Django-based web application for managing clients and CM licenses for the Stratus Report Generator.

## Overview

The Stratus Report Generator is a tool designed to help manage client information and their associated CM licenses. It provides a user-friendly interface for viewing, adding, editing, and deleting client licenses.

## Features

- **Client Management**: View a list of all clients with their details
- **License Management**: Add, edit, and delete CM licenses for clients
- **User Authentication**: Secure login with Google OAuth
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Mode Support**: Toggle between light and dark themes

## Installation

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tools-incubeta-operations-stratus-reportgenerator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Access the application at `http://localhost:8000`

3. Log in using your Google account

4. Navigate to the Clients page to view and manage clients

5. Click on a client to view their details and manage their licenses

## Project Structure

- `app/`: Main application directory
  - `models/`: Database models (Client, Country, CmLicense)
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JS, images)
  - `views.py`: View functions
  - `admin.py`: Admin site configuration
  - `forms.py`: Form definitions

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Authentication**: Google OAuth via social-auth-app-django
- **Database**: SQLite (development) / PostgreSQL (production)

## License Management

The application allows you to:

1. View all clients in a table format
2. View detailed information about each client
3. Add new CM licenses to clients
4. Edit existing CM licenses
5. Delete CM licenses

## Theme Support

The application supports both light and dark themes. Users can toggle between themes using the moon/sun icon in the navigation bar.
