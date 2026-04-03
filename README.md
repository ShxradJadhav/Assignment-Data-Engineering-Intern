# 🏢 B2B Job Market Intelligence Pipeline

## 🚀 LIVE STATUS: [✅ ONLINE]
- **Live API Endpoint:** [https://assignment-data-engineering-intern.onrender.com/jobs](https://assignment-data-engineering-intern.onrender.com/jobs)
- **Interactive Documentation:** [https://assignment-data-engineering-intern.onrender.com/docs](https://assignment-data-engineering-intern.onrender.com/docs)
---
# 🏢 B2B Job Market Intelligence Pipeline

> A fully automated data pipeline that scrapes, cleans, stores, and serves job listing data via a REST API — built as a Data Engineering Intern assignment.

---

## 📌 Problem Statement

Businesses — especially recruitment agencies, HR tech platforms, and talent analytics firms — need **real-time visibility into job market trends**. Manually tracking job postings across platforms is slow, inconsistent, and unscalable.

This project builds an end-to-end **automated data pipeline** that:
- Scrapes structured job listing data from a public source
- Cleans and standardizes the data
- Loads it into a relational database
- Exposes it via a live REST API — ready for dashboards, CRMs, or downstream analytics

---

## 🗂️ Project Structure

```
Web_Scrapper_project/
│
├── scraper.py           # Phase 1: Scrapes job listings, exports raw CSV
├── clean_data.py        # Phase 2: Cleans and standardizes the raw data
├── load_data.py         # Phase 2: Loads cleaned data into MySQL
├── run_pipeline.py      # Automation: Runs all 3 steps in sequence
├── api.py               # Phase 3: FastAPI REST endpoint
│
├── data/
│   └── clean/
│       └── jobs_clean.csv   # Cleaned output (auto-generated)
│
├── jobs_fake_python.csv     # Raw scraped data (auto-generated)
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Tool |
|---|---|
| Scraping | Python, `requests`, `BeautifulSoup` |
| Data Cleaning | `pandas` |
| Database | MySQL |
| API | FastAPI |
| Automation | Python `os.system()` orchestrator |

---

## 🔄 Pipeline Overview

```
[Public Web Source]
       │
       ▼
  scraper.py          →  jobs_fake_python.csv   (raw)
       │
       ▼
  clean_data.py       →  data/clean/jobs_clean.csv   (standardized)
       │
       ▼
  load_data.py        →  MySQL: CleanDB.final_jfp   (stored)
       │
       ▼
  api.py              →  GET /jobs   (served)
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- MySQL Server (running locally)
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Web_Scrapper_project.git
cd Web_Scrapper_project
```

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 pandas mysql-connector-python fastapi uvicorn
```

### 3. Set Up MySQL Database

Log into MySQL and run:

```sql
CREATE DATABASE CleanDB;
USE CleanDB;

CREATE TABLE final_jfp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    job_link TEXT,
    region VARCHAR(10)
);
```

### 4. Configure Environment Variables

Update the database credentials in `load_data.py` and `api.py`:

```python
host     = "localhost"
user     = "root"
password = "your_password"   # ← change this
database = "CleanDB"
```

> **Tip:** For production, move these to a `.env` file and use `python-dotenv` to load them.

### 5. Run the Full Pipeline

```bash
python run_pipeline.py
```

This runs all three steps automatically:
1. Scrapes job listings → saves raw CSV
2. Cleans the data → saves clean CSV
3. Loads clean data → inserts into MySQL

### 6. Start the API

```bash
uvicorn api:app --reload
```

Visit: [http://127.0.0.1:8000/jobs](http://127.0.0.1:8000/jobs)

Auto-generated API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Reference

## 📊 Live Dashboard

An interactive dashboard visualizing the scraped job data — filterable by region, role type, and keyword search.

👉 [View Dashboard](https://shxradjadhav.github.io/Web_Scrapper_project/dashboard.html)

<img width="1893" height="761" alt="image" src="https://github.com/user-attachments/assets/bdcbd773-6ea8-4636-ad02-56a09cbba129" />
<img width="1881" height="875" alt="image" src="https://github.com/user-attachments/assets/3ad3b859-0c78-4c79-9703-e4cf9bfe6cb8" />


### `GET /jobs`

Returns the latest 50 job listings from the database.

**Sample Response:**

```json
[
  [1, "software developer", "Hallman-Metz", "Cynthiachester, TX", "https://...", "TX"],
  [2, "data analyst", "Ryan LLC", "Port Davidmouth, NY", "https://...", "NY"]
]
```

---

## 🧹 Data Cleaning — Decisions Documented

| Step | Decision |
|---|---|
| Exact duplicates | Dropped with `drop_duplicates()` |
| Whitespace | Stripped from all string fields |
| Job titles | Lowercased for consistency |
| Missing values | Filled with `"Unknown"` |
| Region extraction | Parsed 2-letter state code from end of location string using regex `([A-Z]{2})$` |
| Newline characters | Replaced with spaces to prevent CSV layout breaks |

---

## 🤖 Automation

`run_pipeline.py` chains all three scripts in sequence using `os.system()`:

```python
os.system("python scraper.py")
os.system("python clean_data.py")
os.system("python load_data.py")
```

To schedule this pipeline to run automatically (e.g., daily):

**On Linux/macOS — use cron:**
```bash
crontab -e
# Add this line to run every day at 8 AM:
0 8 * * * /usr/bin/python3 /path/to/run_pipeline.py
```

**On Windows — use Task Scheduler:**
- Program: `python`
- Arguments: `C:\path\to\run_pipeline.py`
- Trigger: Daily

---

## 📊 B2B Use Cases

This pipeline can deliver value to:

| Business | Use Case |
|---|---|
| Recruitment agencies | Track which roles are in demand by region |
| HR analytics platforms | Monitor hiring trends over time |
| Salary benchmarking tools | Combine with salary data for compensation insights |
| B2B SaaS tools | Feed job data into CRM or outreach workflows |

---

## 🧠 Bonus: AI/ML Layer (Conceptual Write-Up)

### Proposed Enhancement: Job Category Classifier

**What:** Use a pre-trained NLP model (e.g., `sentence-transformers` or OpenAI embeddings) to automatically classify each job title into a standardized category (e.g., Engineering, Marketing, Finance).

**Why:**
- Raw job titles are inconsistent — "Sr. SWE", "Software Engineer III", and "Dev" all mean the same thing
- Categorized data is far more useful for downstream analytics and filtering

**Approach:**
- Embed job titles using `sentence-transformers/all-MiniLM-L6-v2`
- Cluster similar titles using K-Means or cosine similarity
- Label clusters manually once, then auto-classify new titles

**Trade-offs:**

| Trade-off | Consideration |
|---|---|
| Accuracy vs. Speed | Larger models (GPT-4) = higher accuracy but slower/expensive |
| Zero-shot vs. Fine-tuned | Zero-shot is faster to deploy; fine-tuned on job data performs better |
| Rule-based fallback | A regex/keyword fallback handles edge cases cheaply |

---

## 📝 Environment Variables Reference

| Variable | Description | Default |
|---|---|---|
| `DB_HOST` | MySQL host | `localhost` |
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | MySQL password | *(required)* |
| `DB_NAME` | Database name | `CleanDB` |

---

## 🏗️ Future Improvements

- Move credentials to `.env` using `python-dotenv`
- Add pagination support for multi-page sources
- Add logging with timestamps for each pipeline run
- Dockerize the full stack for one-command deployment
- Add a simple frontend dashboard (React or Streamlit)
- Implement deduplication at the DB level to support repeated runs safely

---

## 👤 Author

**Sharad Jadhav**
Data Engineering Intern Assignment
