# Library Management System

This is a Django-based Library Management System API that allows users to manage library users, books, and borrow records. The project provides RESTful APIs for creating, listing, and updating library users, books, and borrow records.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
  - [Library Users](#library-users)
  - [Books](#books)
  - [Borrow Records](#borrow-records)
  - [Authentication](#authentication)
- [API Documentation](#api-documentation)
- [Admin Panel](#admin-panel)
- [User Authentication](#user-authentication)
- [Permissions](#permissions)
- [Additional Notes](#additional-notes)

## Project Structure

The project is organized into the following components:

- `BorrowingBooks`: The main Django app containing models, views, serializers, and permissions.
- `rest_framework`, `dj_rest_auth`: Django REST Framework and Django REST Auth for authentication and API views.
- `drf_yasg`: Swagger and ReDoc for API documentation.
- `allauth`: Allauth for user registration.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hamzaderbaz/Borrowing-Books.git
   cd Borrowing-Books
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at [http://localhost:8000/api/](http://localhost:8000/api/)

## API Endpoints

### Library Users

- **List/Create Library Users:** [http://localhost:8000/api/library-users/](http://localhost:8000/api/library-users/)
  - `GET`: Retrieve a list of all library users.
  - `POST`: Create a new library user.

### Books

- **List/Create Books:** [http://localhost:8000/api/books/](http://localhost:8000/api/books/)
  - `GET`: Retrieve a list of all books.
  - `POST`: Create a new book.

### Borrow Records

- **List/Create Borrow Records:** [http://localhost:8000/api/borrow-records/](http://localhost:8000/api/borrow-records/)
  - `GET`: Retrieve a list of all borrow records.
  - `POST`: Create a new borrow record.

- **Retrieve/Update Borrow Record:** [http://localhost:8000/api/borrow-records/{id}/](http://localhost:8000/api/borrow-records/{id}/)
  - `GET`: Retrieve details of a specific borrow record.
  - `PUT/PATCH`: Update details of a specific borrow record.

### Authentication

- **User Login:** [http://localhost:8000/api/auth/login/](http://localhost:8000/api/auth/login/)
  - `POST`: Log in a user. Requires a valid username and password.

- **User Registration:** [http://localhost:8000/api/auth/registration/](http://localhost:8000/api/auth/registration/)
  - `POST`: Register a new user. Requires a valid username, email, and password.

## API Documentation

Explore the API using the following documentation tools:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
  - Swagger UI provides an interactive and user-friendly interface for exploring and testing API endpoints. It includes detailed information about each endpoint, request methods, request and response parameters, and example requests and responses.

- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
  - ReDoc offers a clean and visually appealing documentation interface. It provides a structured overview of the API, including details about resource endpoints, request and response formats, and additional information such as data types and examples.

## Admin Panel

Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage library users, books, and borrow records conveniently.

## Permissions

- **LibraryUserListCreateView:**
  - List/Create library users.
  - Requires authentication but allows read-only access for unauthenticated users.

- **BookListCreateView:**
  - List/Create books.
  - Requires authentication and ownership to create books.

- **BorrowRecordListCreateView:**
  - List/Create borrow records.
  - Requires ownership to create borrow records.

- **BorrowRecordRetrieveUpdateView:**
  - Retrieve/Update borrow records.
  - Requires ownership to update borrow records.


## Additional Notes

- The project uses Token Authentication and JWT Authentication.
- API documentation is provided using Swagger and ReDoc.
- User registration is handled using Allauth.
- Throttling is implemented with default rates.
- The project includes Swagger and ReDoc UIs for easy API exploration.

Feel free to explore the API documentation and use the provided endpoints to manage your library system efficiently. If you encounter any issues or have questions, refer to the [Django documentation](https://docs.djangoproject.com/) or contact the project maintainer.


