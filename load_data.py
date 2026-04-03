import pandas as pd
import sqlite3

# Load cleaned data (USE RELATIVE PATH — VERY IMPORTANT)
df = pd.read_csv("data/clean/jobs_clean.csv")

# Connect to SQLite (creates file if not exists)
conn = sqlite3.connect("jobs.db")

# Load data into table
df.to_sql("final_jfp", conn, if_exists="replace", index=False)

print(f"{len(df)} records inserted into SQLite.")

# Close connection
conn.close()
