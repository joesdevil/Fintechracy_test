# Django Receipt Tracker

This is a simple Django application that allows users to manually enter and track their receipt information.

## Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd receipt_tracker
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

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

## Tests

To run tests, use the following command:

```bash
python manage.py test
