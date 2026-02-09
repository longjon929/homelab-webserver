# Homelab Webserver

This project is a Python web server using FastAPI that provides an API to interact with a PostgreSQL database.

## Features

- **FastAPI Backend**: A modern, fast (high-performance) web framework for building APIs.
- **PostgreSQL Integration**: Uses SQLAlchemy for ORM and psycopg2 as the database driver.
- **Database Migrations**: Alembic is configured for handling database schema migrations.
- **CSV Upload**: An endpoint to upload CSV files and import data into the database.
- **Environment-based Configuration**: API secrets and database connection strings are managed via a `.env` file.

## Project Structure

```
├── app/                  # Main application directory
│   ├── crud.py           # Database CRUD operations
│   ├── database.py       # Database connection and session management
│   ├── main.py           # FastAPI application and endpoints
│   ├── models.py         # SQLAlchemy database models
│   └── schemas.py        # Pydantic schemas for data validation
├── migrations/           # Alembic database migrations
│   ├── versions/         # Migration scripts
│   ├── env.py            # Alembic environment configuration
│   └── ...
├── .env                  # Environment variables (gitignored)
├── alembic.ini           # Alembic configuration
├── pyproject.toml        # Project metadata and dependencies
├── README.md             # This file
└── ...
```

## Getting Started

### Prerequisites

- Python 3.12+
- `uv` for package management
- A running PostgreSQL database instance

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd homelab-webserver
    ```

2.  **Install dependencies:**
    The project uses `uv` for dependency management. The dependencies are listed in `pyproject.toml`.
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Configure the database:**
    - Create a `.env` file in the project root by copying the example:
      ```bash
      cp .env.example .env
      ```
    - Edit the `.env` file and set the `DATABASE_URL` to your PostgreSQL connection string.
      ```
      DATABASE_URL="postgresql://user:password@localhost/dbname"
      ```

4.  **Run database migrations:**
    Once the database is configured, apply the migrations to create the initial tables.
    ```bash
    alembic upgrade head
    ```

### Running the Application

To run the application, use `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **`GET /`**: Welcome message.
- **`POST /items/`**: Create a new item.
- **`GET /items/`**: Get a list of items.
- **`GET /items/{item_id}`**: Get a specific item by ID.
- **`POST /upload-csv/`**: Upload a CSV file to import data. The CSV file must have a header with `name,description`.

### Example CSV Upload

You can use `curl` to upload a CSV file:

```bash
curl -X POST -F "file=@/path/to/your/data.csv" http://127.0.0.1:8000/upload-csv/
```