from .database import get_db_connection
from . import schemas
import psycopg2.extras


# --- Sensors ---
def get_sensor(conn, sensor_id: int):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM sensors WHERE id = %s", (sensor_id,))
        return cur.fetchone()


def get_sensors(conn, skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM sensors ORDER BY id LIMIT %s OFFSET %s", (limit, skip))
        return cur.fetchall()


def create_sensor(conn, sensor: schemas.SensorCreate):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "INSERT INTO sensors (name, model) VALUES (%s, %s) RETURNING *",
            (sensor.name, sensor.model),
        )
        new_sensor = cur.fetchone()
        conn.commit()
        return new_sensor


# --- Locations ---
def get_location(conn, location_id: int):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM locations WHERE id = %s", (location_id,))
        return cur.fetchone()


def get_locations(conn, skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM locations ORDER BY id LIMIT %s OFFSET %s", (limit, skip))
        return cur.fetchall()


def create_location(conn, location: schemas.LocationCreate):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "INSERT INTO locations (name) VALUES (%s) RETURNING *",
            (location.name,),
        )
        new_location = cur.fetchone()
        conn.commit()
        return new_location


# --- Environment Data ---
def get_environment_data(conn, env_id: int):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM environment_data WHERE id = %s", (env_id,))
        return cur.fetchone()


def get_environment_data_list(conn, skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "SELECT * FROM environment_data ORDER BY recorded_at DESC LIMIT %s OFFSET %s",
            (limit, skip),
        )
        return cur.fetchall()


def create_environment_data(conn, data: schemas.EnvironmentDataCreate):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            """
            INSERT INTO environment_data (sensor_id, location_id, temperature, humidity, pressure, co2)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING *
            """,
            (
                data.sensor_id,
                data.location_id,
                data.temperature,
                data.humidity,
                data.pressure,
                data.co2,
            ),
        )
        new_data = cur.fetchone()
        conn.commit()
        return new_data


# --- Soil Data ---
def get_soil_data(conn, soil_id: int):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM soil_data WHERE id = %s", (soil_id,))
        return cur.fetchone()


def get_soil_data_list(conn, skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "SELECT * FROM soil_data ORDER BY recorded_at DESC LIMIT %s OFFSET %s",
            (limit, skip),
        )
        return cur.fetchall()


def create_soil_data(conn, data: schemas.SoilDataCreate):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            """
            INSERT INTO soil_data (sensor_id, location_id, moisture)
            VALUES (%s, %s, %s) RETURNING *
            """,
            (data.sensor_id, data.location_id, data.moisture),
        )
        new_data = cur.fetchone()
        conn.commit()
        return new_data
