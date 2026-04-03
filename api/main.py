from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

# Path to the cleaned data
CSV_PATH = "data/clean/jobs_clean.csv"

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
