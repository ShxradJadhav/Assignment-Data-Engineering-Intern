# Assignment-Data-Engineering-Intern

# 🚀 Job Market Intelligence Pipeline (Web Scraper + ETL + API)

## 📌 Overview

Businesses often lack real-time visibility into hiring trends, competitor activity, and job market demand. This project solves that problem by building an **end-to-end data pipeline** that:

* Scrapes job data from a public source
* Cleans and standardizes the data
* Stores it in a structured database
* Exposes it via an API for real-time access

The system is designed to run automatically and deliver **reliable, queryable insights**.

---

## 💼 Problem Statement

Organizations need access to external job market data to:

* Track competitor hiring trends
* Identify demand for specific roles
* Understand regional hiring patterns

However, this data is not readily available in structured form.

👉 This project builds a **dynamic data pipeline** to bridge that gap.

---

## 🧱 Architecture

```
Scraper → Raw Data → Cleaning → MySQL DB → FastAPI → User/API
```

### Flow:

1. Scraper collects job listings
2. Data is cleaned and standardized
3. Stored in MySQL database
4. API serves data to users dynamically

---

## ⚙️ Tech Stack

* **Python**
* **BeautifulSoup / Requests** (Web Scraping)
* **Pandas** (Data Cleaning)
* **MySQL** (Database)
* **FastAPI** (API Layer)
* **OS / Scheduler** (Pipeline Automation)

---

## 🔍 Features

### ✅ Web Scraping

* Extracts job title, company, location, link
* Handles pagination
* Handles missing fields and failures

### ✅ Data Cleaning

* Removes duplicates
* Standardizes text formats
* Handles null values
* Extracts region from location

### ✅ Database Storage

* Stores cleaned data in MySQL
* Optimized bulk insertion
* Avoids duplicate entries

### ✅ API Layer

* Fetch jobs dynamically
* Supports filters (location, limit)

Example:

```
GET /jobs?location=Remote&limit=10
```

---

## 📊 API Endpoints

### 🔹 Get Jobs

```
GET /jobs
```

### 🔹 Filtered Jobs

```
GET /jobs?location=New York&limit=20
```

### 🔹 Jobs by Region

```
GET /jobs/region
```

---

## 🛠️ Project Structure

```
project/
│
├── scraper.py
├── clean_data.py
├── load_data.py
├── pipeline.py
│
├── data/
│   ├── raw/
│   └── clean/
│
├── api/
│   └── main.py
│
└── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone Repo

```
git clone <your-repo-link>
cd project
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=CleanDB
```

---

### 4. Run Pipeline

```
python pipeline.py
```

---

### 5. Run API

```
uvicorn main:app --reload
```

👉 Open:

```
http://127.0.0.1:8000/docs
```

---

## ⏱️ Automation

The pipeline can be scheduled using:

* Cron jobs (Linux/Mac)
* Task Scheduler (Windows)

Example:

```
Runs every 6 hours to keep data updated
```

---

## 🤖 Bonus (Intelligence Layer)

Basic insights added:

* Job distribution by region
* Filtering for targeted analysis

Future improvements:

* Trend detection
* Salary prediction
* Role demand forecasting

---

## ⚖️ Trade-offs

* Used MySQL for simplicity over distributed systems
* Basic scraping instead of headless browser (faster execution)
* Focused on reliability over complexity due to time constraint

---

## 📈 Future Enhancements

* Add real-time streaming (Kafka)
* Deploy on cloud (AWS/Azure)
* Add frontend dashboard
* Integrate ML for job trend predictions

---

## 👨‍💻 Author

**Sharad Jadhav**
Data Engineer | Python | SQL | Azure

---

## ⭐ Conclusion

This project demonstrates:

* End-to-end data pipeline design
* Data cleaning and transformation
* Backend API development
* Practical business use-case implementation

👉 Built with a focus on **scalability, automation, and usability**.
