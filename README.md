# Restful API Book Project

This project is a Django RESTful API for managing toys and drones, including their categories, pilots, and competitions. It demonstrates the use of Django, Django REST Framework, and PostgreSQL for building a modular, scalable API.

## Features
- RESTful API endpoints for managing toys, drones, drone categories, pilots, and competitions
- CRUD operations for all main entities
- Modular Django app structure (`toys`, `drones`)
- Uses Django REST Framework for serialization and API views
- PostgreSQL as the database backend

## Project Structure
- `restful01/` - Main Django project settings and configuration
- `toys/` - App for managing toys
- `drones/` - App for managing drones, categories, pilots, and competitions
- `manage.py` - Django project management script

## Models
### Toys
- `Toy`
  - `created`: DateTime, auto-set on creation
  - `name`: CharField
  - `description`: TextField
  - `toy_category`: CharField
  - `release_date`: DateTime
  - `was_included_in_home`: Boolean
  - Meta: ordered by `name`

### Drones
- `DroneCategory`
  - `name`: CharField
  - Meta: ordered by `name`
- `Drone`
  - `name`: CharField
  - `drone_category`: ForeignKey to `DroneCategory`
  - `manufacturing_date`: DateTime
  - `has_it_completed_missions`: Boolean
  - `inserted_timestamp`: DateTime, auto-set on creation
  - Meta: ordered by `name`
- `Pilot`
  - `name`: CharField
  - `gender`: CharField (choices: Male/Female)
  - `reces_count`: Integer
  - `inserted_timestamp`: DateTime, auto-set on creation
  - Meta: ordered by `name`
- `Competition`
  - `pilot`: ForeignKey to `Pilot`
  - `drone`: ForeignKey to `Drone`
  - `distance_in_feet`: Integer
  - `distance_achievement_date`: DateTime
  - Meta: ordered by `-distance_in_feet`

## API Endpoints

### Toys
- `GET /toys/` - List all toys
- `POST /toys/` - Create a new toy
- `GET /toys/<id>/` - Retrieve a toy
- `PUT /toys/<id>/` - Update a toy
- `DELETE /toys/<id>/` - Delete a toy

### Drones
- `GET /drones/drone-categories/` - List all drone categories
- `POST /drones/drone-categories/` - Create a new drone category
- `GET /drones/drone-categories/<id>/` - Retrieve, update, or delete a drone category
- `GET /drones/drones/` - List all drones
- `POST /drones/drones/` - Create a new drone
- `GET /drones/drones/<id>/` - Retrieve, update, or delete a drone
- `GET /drones/pilots/` - List all pilots
- `POST /drones/pilots/` - Create a new pilot
- `GET /drones/pilots/<id>/` - Retrieve, update, or delete a pilot
- `GET /drones/competitions/` - List all competitions
- `POST /drones/competitions/` - Create a new competition
- `GET /drones/competitions/<id>/` - Retrieve, update, or delete a competition
- `GET /drones/` - API root with links to all endpoints

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies** (create a virtual environment and install Django and Django REST Framework):
   ```bash
   pip install django djangorestframework psycopg2-binary
   ```
3. **Configure PostgreSQL**
   - Ensure PostgreSQL is running and a database named `drones` exists.
   - Update `restful01/settings.py` with your DB credentials if needed.
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. **Access the API**
   - Toys endpoints: `http://localhost:8000/toys/`
   - Drones endpoints: `http://localhost:8000/drones/`

## Dependencies
- Python 3.x
- Django >= 5.2.2
- djangorestframework
- psycopg2-binary (for PostgreSQL)

## Notes
- The project uses Django's default admin at `/admin/`.
- You may need to create a superuser for admin access:
  ```bash
  python manage.py createsuperuser
  ```

---

For more details, see the code in each app's `models.py`, `views.py`, and `urls.py` files.


    