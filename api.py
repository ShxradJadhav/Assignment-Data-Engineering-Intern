from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

# This finds the folder where api.py is located and joins it with the data path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "clean", "jobs_clean.csv")

@app.get("/")
def home():
    return {"status": "Online", "message": "B2B Job Market API is live"}

@app.get("/jobs")
def get_jobs():
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        # Convert dataframe to dictionary for JSON output
        return df.to_dict(orient="records")
    return {"error": "Data file not found. Run pipeline first."}
