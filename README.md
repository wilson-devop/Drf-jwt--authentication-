#  DRF JWT Authentication System

A RESTful authentication API built using **Django REST Framework (DRF) and Simple JWT. This project implements token-based authentication and provides a foundation for securing backend applications.

The API endpoints have been tested using Postman.

## Technologies Used

 Python
 Django
 Django REST Framework
 Simple JWT- PostgreSQL / SQLite (depending on configuration)
 Postman
 Git and GitHub

## Features

User registration
 User login
 JWT-based authentication
 Access token generation
 Refresh token functionality
 Protected API endpoints
 Token-based authorization
 API testing using Postman

*Update this list to reflect the exact features implemented in your project.*

## Project Structure


nwm/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── ...
```

*Your actual application and configuration folder names may differ.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/wilson-devop/Drf-jwt--authentication-.git
```

### 2. Navigate into the project

```bash
cd Drf-jwt--authentication-
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root and add the environment variables required by your Django settings.

Example:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Use the actual variable names expected by your `settings.py`. Do not commit your `.env` file.

### 7. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

### 9. Start the development server

```bash
python manage.py runserver
```

The API will normally be accessible at:

```text
http://127.0.0.1:8000/
```

##  Authentication Workflow

This project uses JSON Web Tokens (JWT) through Simple JWT.

The authentication process generally follows these steps:

1. A user creates an account through the registration endpoint.
2. The user submits login credentials.
3. The server validates the credentials.
4. The server issues an access token and a refresh token.
5. The client uses the access token to access protected endpoints.
6. When the access token expires, the refresh token can be used to obtain a new access token.

### JWT Token Types

| Token | Purpose |
|---|---|
| Access Token | Authorizes requests to protected endpoints |
| Refresh Token | Obtains a new access token |

For protected endpoints, include the access token in the request header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## API Endpoints

The following table is a documentation template. Replace the placeholders with the actual routes configured in your project.

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/your-register-route/` | Register a user | Not required |
| POST | `/your-login-route/` | Authenticate a user | Not required |
| POST | `/your-refresh-route/` | Refresh access token | Refresh token |
| POST | `/your-logout-route/` | Log out a user | Depends on implementation |
| GET | `/your-profile-route/` | Retrieve user profile | Required |

### Example: Login Request

```json
{
    "username": "example_user",
    "password": "your_password"
}
```

The actual request fields depend on your login serializer.

### Example: JWT Authorization Header

```http
Authorization: Bearer <access_token>
```

## Testing With Postman

All implemented authentication endpoints have been tested using Postman.

To test the API:

1. Start the Django development server.
2. Open Postman.
3. Create a request using the appropriate HTTP method.
4. Enter the API endpoint.
5. Provide the required request body.
6. Test registration and login.
7. Copy the access token returned by the login endpoint.
8. Open the Authorization tab.
9. Select Bearer Token.
10. Paste the access token and test protected endpoints.

Verify the following:

- Successful user registration.
- Successful login with valid credentials.
- Rejection of invalid login credentials.
- Successful access to protected endpoints with a valid token.
- Rejection of unauthorized requests.
- Successful token refresh, where implemented.

## Security Considerations

- Never expose Django SECRET_KEY.
- Never upload database credentials.
- Keep `.env` files out of version control.
- Do not expose production credentials in API responses.
- Use HTTPS in production.
- Set `DEBUG=False` in production.
- Configure appropriate JWT token lifetimes and permissions.

## Future Improvements

Potential improvements include:

- Email verification.
- Password reset functionality.
- Role-based access control.
- Rate limiting.
- Automated API tests.
- API documentation using Swagger/OpenAPI.
- Production deployment.

## Author

**Wilson Mbuyu**

Backend & Mobile Developer

- GitHub: [wilson-devop](https://github.com/wilson-devop)
- LinkedIn: [Wilson Mbuyu](https://www.linkedin.com/in/wilson-mbuyu-940544358/)

