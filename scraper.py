import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

jobs = []

base_url = "https://realpython.github.io/fake-jobs/"

try:
    print("[INFO] Sending request...")
    response = requests.get(base_url, timeout=10)
    response.raise_for_status()
except Exception as e:
    print(f"[ERROR] Failed to fetch page: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

listings = soup.find_all("div", class_="card-content")

print(f"[INFO] Found {len(listings)} job listings")

for job in listings:
    try:
        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")
        link = job.find("a")

        jobs.append({
            "title": title.text.strip() if title else "Unknown",
            "company": company.text.strip() if company else "Unknown",
            "location": location.text.strip() if location else "Unknown",
            "job_link": link["href"] if link else "Unknown"
        })

    except Exception as e:
        print(f"[WARNING] Skipping a job due to error: {e}")

df = pd.DataFrame(jobs)

df.to_csv("jobs_fake_python.csv", index=False)

print(f"[INFO] Data saved successfully ({len(df)} records)")
