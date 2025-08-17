from fastapi import FastAPI
import mysql.connector
import os

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "125612567")
DB_NAME = os.getenv("DB_NAME", "mysql-db")

def connect_to_db():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME*  )
    return conn

app = FastAPI()

@app.get("/")
def load_table():
    query = 'SELECT * FROM table_for_project;'
    try:
        conn = connect_to_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        return {"data": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
