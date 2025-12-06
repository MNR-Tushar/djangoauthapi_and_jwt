# Django REST API with JWT Authentication

A robust Django REST Framework API with JWT (JSON Web Token) authentication, featuring user registration, login, profile management, and password change functionality.

## Features

- **Custom User Model** - Email-based authentication instead of username
- **JWT Authentication** - Secure token-based authentication using Simple JWT
- **User Registration** - Create new user accounts with email and password
- **User Login** - Authenticate and receive JWT tokens
- **User Profile** - View and update user profile information
- **Password Management** - Change password with old password verification
- **Admin Panel** - Full admin interface for user management
- **CORS Support** - Cross-Origin Resource Sharing enabled
- **Token Refresh** - Refresh access tokens without re-authentication

## Tech Stack

- **Django** 5.1.7
- **Django REST Framework** 3.16.1
- **djangorestframework-simplejwt** 5.5.1
- **django-cors-headers** 4.9.0
- **Python** 3.x
- **SQLite** (default database)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd djangoauthapi_and_jwt
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/register/` | Register a new user | No |
| POST | `/login/` | Login and get JWT tokens | No |
| POST | `/token/refresh/` | Refresh access token | No |
| GET | `/profile/` | Get user profile | Yes |
| POST | `/change-password/` | Change user password | Yes |

### Admin Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/users/` | List all users | Admin only |
| POST | `/users/` | Create a new user | Admin only |
| GET | `/users/{id}/` | Get user details | Admin only |
| PUT | `/users/{id}/` | Update user | Admin only |
| PATCH | `/users/{id}/` | Partial update user | Admin only |
| DELETE | `/users/{id}/` | Delete user | Admin only |

## API Usage Examples

### 1. User Registration

**Request:**
```bash
POST /register/
Content-Type: application/json

{
    "email": "user@example.com",
    "name": "John Doe",
    "password": "securePassword123",
    "password2": "securePassword123"
}
```

**Response:**
```json
{
    "token": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    },
    "message": "Registration Successful",
    "user": {
        "email": "user@example.com",
        "name": "John Doe"
    }
}
```

### 2. User Login

**Request:**
```bash
POST /login/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "securePassword123"
}
```

**Response:**
```json
{
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "is_active": true,
    "is_staff": false,
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
}
```

### 3. Get User Profile

**Request:**
```bash
GET /profile/
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "is_active": true,
    "created_at": "2025-12-03T17:59:00Z"
}
```

### 4. Change Password

**Request:**
```bash
POST /change-password/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "old_password": "securePassword123",
    "password": "newSecurePassword456",
    "password2": "newSecurePassword456"
}
```

**Response:**
```json
{
    "message": "Password changed successfully"
}
```

### 5. Refresh Token

**Request:**
```bash
POST /token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## Authentication

This API uses JWT (JSON Web Token) authentication. After logging in or registering, you'll receive two tokens:

- **Access Token**: Short-lived token (20 minutes) used for API requests
- **Refresh Token**: Long-lived token (1 day) used to obtain new access tokens

### Using Tokens

Include the access token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

### Token Expiration

- **Access Token**: Expires after 20 minutes
- **Refresh Token**: Expires after 1 day

When the access token expires, use the refresh token to get a new access token without requiring the user to log in again.

## Configuration

### JWT Settings

You can modify JWT settings in `djangoauthapi_and_jwt/settings.py`:

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    # ... other settings
}
```

### CORS Settings

Allowed origins can be configured in `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]
```

## User Model

The custom user model includes:

- `email` - Unique email address (used for authentication)
- `name` - User's full name
- `password` - Hashed password
- `is_active` - Account active status
- `is_staff` - Staff status
- `is_superuser` - Superuser status
- `created_at` - Account creation timestamp
- `updated_at` - Last update timestamp
- `deleted_at` - Soft delete timestamp (nullable)

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/`

Features:
- View and manage all users
- Search users by email and name
- Filter users by status
- View creation and update timestamps

## Testing

Run the test suite:

```bash
python manage.py test
```

## Security Considerations

- Never commit the `SECRET_KEY` to version control
- Use environment variables for sensitive information
- Set `DEBUG = False` in production
- Configure proper `ALLOWED_HOSTS` for production
- Use HTTPS in production
- Implement rate limiting for authentication endpoints
- Consider using token blacklisting for logout functionality

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False`
2. Update `SECRET_KEY` with a strong, unique key
3. Configure `ALLOWED_HOSTS`
4. Use a production-grade database (PostgreSQL, MySQL)
5. Set up proper CORS policies
6. Use environment variables for configuration
7. Implement proper logging
8. Set up HTTPS/SSL
9. Configure static and media files serving

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'rest_framework'`
- **Solution**: Install dependencies using `pip install -r requirements.txt`

**Issue**: `OperationalError: no such table`
- **Solution**: Run migrations: `python manage.py migrate`

**Issue**: Token authentication not working
- **Solution**: Ensure the Authorization header is properly formatted: `Bearer <token>`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please open an issue in the repository.

## Acknowledgments

- Django REST Framework documentation
- Simple JWT documentation
- Django documentation