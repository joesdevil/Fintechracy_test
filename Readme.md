# Django Receipt Tracker

This is a simple Django application that allows users to manually enter and track their receipt information.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/joesdevil/Fintechracy_test
    cd Fintechracy_test
    ```

2. Create and activate a virtual environment :

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    this app depend only on django so there is no requirements.txt file

    ```bash
    pip install django
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    this user you can make access with it 

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Visit the admin site [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to add/edit users and receipts.
- Use the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

 