# Django RESTful API Project

A comprehensive Django RESTful API project for managing toys and drones, including their categories, pilots, and competitions. This project demonstrates advanced Django REST Framework features, custom permissions, filtering, pagination, and API versioning.

## 🚀 Features

### Core Features
- **RESTful API endpoints** for managing toys, drones, drone categories, pilots, and competitions
- **CRUD operations** for all main entities with proper HTTP methods
- **Modular Django app structure** (`toys`, `drones`)
- **Django REST Framework** for serialization and API views
- **PostgreSQL** as the database backend
- **Custom pagination** with upper bound limit
- **Advanced filtering** using Django Filter Backend
- **Search and ordering** functionality
- **Token-based authentication** for pilot endpoints
- **Custom permissions** for drone management
- **API versioning** support (v1 and v2)
- **Rate limiting** with configurable throttling
- **CORS support** for cross-origin requests
- **Environment variables** support for secure configuration

### Advanced Features
- **Custom pagination class** with maximum limit enforcement
- **Custom permission classes** for object-level permissions
- **Advanced filtering** with date ranges and numeric filters
- **API versioning** with namespace-based versioning
- **Rate throttling** with different limits for different user types
- **Comprehensive test suite** with pytest configuration

## 📁 Project Structure

```
src/
├── restful01/                 # Main Django project settings
│   ├── __init__.py
│   ├── settings.py           # Project configuration
│   ├── urls.py              # Main URL configuration
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── toys/                     # Toys app
│   ├── __init__.py
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Toy model
│   ├── serializers.py       # Toy serializers
│   ├── views.py             # Toy views
│   ├── urls.py              # Toy URL patterns
│   ├── tests.py             # Toy tests
│   └── migrations/          # Database migrations
├── drones/                   # Drones app (main app)
│   ├── __init__.py
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Drone-related models
│   ├── serializers.py       # Drone serializers
│   ├── views.py             # Drone views
│   ├── urls.py              # Drone URL patterns
│   ├── tests.py             # Drone tests
│   ├── custompagination.py  # Custom pagination class
│   ├── custompermission.py  # Custom permission classes
│   ├── filters.py           # Custom filters
│   ├── migrations/          # Database migrations
│   └── v2/                  # API version 2
│       ├── urls.py          # V2 URL patterns
│       └── views.py         # V2 views
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies
├── pytest.ini              # Pytest configuration
├── db.sqlite3              # SQLite database (development)
└── README.md               # This file
```


## 🔌 API Endpoints

### Toys Endpoints
- `GET /toys/` - List all toys
- `POST /toys/` - Create a new toy
- `GET /toys/<id>/` - Retrieve a specific toy
- `PUT /toys/<id>/` - Update a toy
- `DELETE /toys/<id>/` - Delete a toy

### Drones Endpoints (v1)
- `GET /drone-categories/` - List all drone categories
- `POST /drone-categories/` - Create a new drone category
- `GET /drone-categories/<id>/` - Retrieve, update, or delete a drone category
- `PUT /drone-categories/<id>/` - Update a drone category
- `DELETE /drone-categories/<id>/` - Delete a drone category

- `GET /drones/` - List all drones
- `POST /drones/` - Create a new drone
- `GET /drones/<id>/` - Retrieve, update, or delete a drone
- `PUT /drones/<id>/` - Update a drone
- `DELETE /drones/<id>/` - Delete a drone

- `GET /pilots/` - List all pilots (requires authentication)
- `POST /pilots/` - Create a new pilot (requires authentication)
- `GET /pilots/<id>/` - Retrieve, update, or delete a pilot (requires authentication)
- `PUT /pilots/<id>/` - Update a pilot (requires authentication)
- `DELETE /pilots/<id>/` - Delete a pilot (requires authentication)

- `GET /competitions/` - List all competitions
- `POST /competitions/` - Create a new competition
- `GET /competitions/<id>/` - Retrieve, update, or delete a competition
- `PUT /competitions/<id>/` - Update a competition
- `DELETE /competitions/<id>/` - Delete a competition

- `GET /` - API root with links to all endpoints

### Drones Endpoints (v2) - Currently Commented Out
- `GET /v2/vehicle-categories/` - List all drone categories (v2 naming)
- `GET /v2/vehicles/` - List all drones (v2 naming)
- `GET /v2/pilots/` - List all pilots (v2)
- `GET /v2/competitions/` - List all competitions (v2)

## 🔧 Custom Components

### Custom Pagination
```python
class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 8
```
- Default page size: 4 items
- Maximum limit: 8 items per request
- Prevents excessive data retrieval

### Custom Permissions
- Only drone owners can update/delete their drones
- Read access for all users
- Applied to drone endpoints

### Custom Filters
- Date range filtering for competitions
- Distance range filtering
- Filter by drone and pilot names

## 🚀 Setup Instructions

### Prerequisites
- Python 3.x
- PostgreSQL
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone <https://github.com/m7md158/Restapibook.git>
cd src
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure PostgreSQL
- Ensure PostgreSQL is running
- Create a database named `drones`
- Update database credentials in `restful01/settings.py` if needed

### 6. Apply Database Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

### 9. Access the Application
- **API Root**: `http://localhost:8000/`
- **Toys API**: `http://localhost:8000/toys/`
- **Drones API**: `http://localhost:8000/drone-categories/`
- **Admin Interface**: `http://localhost:8000/admin/`
- **API Authentication**: `http://localhost:8000/api-auth/`

## 📦 Dependencies

### Core Dependencies
- **Django 5.2.2** - Web framework
- **djangorestframework 3.16.0** - REST API framework
- **psycopg2-binary 2.9.10** - PostgreSQL adapter
- **django-filter 25.1** - Advanced filtering
- **pytest 8.4.1** - Testing framework
- **pytest-django 4.11.1** - Django test integration

### Development Dependencies
- **httpie 3.2.4** - HTTP client for testing
- **requests 2.32.4** - HTTP library
- **rich 14.0.0** - Terminal formatting

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests for specific app
pytest toys/
pytest drones/

# Run tests with coverage
pytest --cov=.
```

### Test Configuration
- Pytest configuration in `pytest.ini`
- Django settings module configured
- Test file patterns: `tests.py`, `test_*.py`, `*_tests.py`

## 🔐 Security Features

### Authentication
- **Token Authentication** for pilot endpoints
- **Session Authentication** for admin interface
- **Basic Authentication** for API access

### Permissions
- **Custom object-level permissions** for drone management
- **User ownership validation** for drone operations
- **Read-only access** for non-owners

### Rate Limiting
- **Anonymous users**: 300 requests/hour
- **Authenticated users**: 100 requests/hour
- **Drone endpoints**: 200 requests/hour
- **Pilot endpoints**: 150 requests/hour

## 🔄 API Versioning

### Current Version (v1)
- Standard endpoint naming
- Full CRUD operations
- All features enabled

### Version 2 (v2) - Currently Disabled
- Alternative endpoint naming (`vehicles` instead of `drones`)
- Same functionality as v1
- Can be enabled by uncommenting v2 URLs in `restful01/urls.py`


### Filtering Competitions
```bash
curl "http://localhost:8000/competitions/?min_distance_in_feet=100&max_distance_in_feet=500"
```

### Pagination
```bash
curl "http://localhost:8000/drones/?limit=4&offset=8"
```

## 🐛 Known Issues

1. **Field Name Typo**: The `Drone` model uses `onwer` instead of `owner` - this is intentional in the current codebase
2. **V2 API Disabled**: Version 2 endpoints are commented out in the main URL configuration
3. **SQLite Database**: The project includes `db.sqlite3` but is configured for PostgreSQL

## 🔧 Development Notes

### Code Quality
- Follows Django best practices
- Uses Django REST Framework conventions
- Implements proper model relationships
- Includes comprehensive serializers

### Performance Considerations
- Custom pagination prevents large data sets
- Database indexing on frequently queried fields
- Efficient filtering with Django Filter Backend

### Scalability
- Modular app structure allows easy extension
- API versioning support for backward compatibility
- Configurable rate limiting
- Environment-based configuration

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Pytest Documentation](https://docs.pytest.org/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## 📄 License

This project is for educational purposes and demonstrates Django REST Framework best practices.

---

**Note**: This project is configured for development. For production deployment, ensure to:
- Set `DEBUG=False`
- Update `ALLOWED_HOSTS`
- Use a strong, unique `SECRET_KEY`
- Configure proper database credentials
- Set up HTTPS
- Configure proper logging
- Set up monitoring and error tracking


    