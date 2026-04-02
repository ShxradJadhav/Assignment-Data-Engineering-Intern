from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/jobs")
def get_jobs():

    conn = mysql.connector.connect(
        host="localhost",
        database="CleanDB",
        user="root",
        password="root"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM final_jfp LIMIT 50")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
