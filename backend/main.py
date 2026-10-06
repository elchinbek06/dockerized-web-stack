import os
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="EPAM Trainee DevOps API")

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "appuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "secretpass")

@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Welcome to Dockerized Web Stack API!",
        "architecture": "Nginx -> FastAPI -> PostgreSQL"
    }

@app.get("/health")
def db_health_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return {"database": "connected", "status": "healthy"}
    except Exception as e:
        return {"database": "disconnected", "error": str(e)}
