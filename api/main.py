from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    conn = sqlite3.connect("jobs.db")  # local file
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM final_jfp LIMIT 50")
    rows = cursor.fetchall()

    conn.close()

    return rows
