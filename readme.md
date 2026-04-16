🚀 Job ETL Pipeline
An end-to-end ETL (Extract, Transform, Load) pipeline that fetches job data from an API, processes it, and stores it in PostgreSQL. The pipeline is automated using Apache Airflow.
---

🧠 Overview
This project demonstrates how to build a real-world data pipeline using Python, PostgreSQL, and Airflow. It extracts job listings from an API, cleans and transforms the data, and loads it into a database for further use.
---

⚙️ Tech Stack
* Python
* PostgreSQL
* Apache Airflow
* REST API (RapidAPI)
---

🔄 Pipeline Flow
Extract → Transform → Load
---

📂 Project Structure
job-etl-pipeline/
│
├── dags/
│   └── dag.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── test_db.py
├── .gitignore
├── README.md

---
🔌 How It Works
 Extract:
Fetches job data from API using Python requests

Transform:
* Cleans text fields
* Removes duplicates
* Standardizes data
* Adds features (e.g., remote jobs flag)

Load:
* Inserts cleaned data into PostgreSQL
* Uses psycopg2 for database connection

---

 ⏱️ Airflow Automation
* DAG automates the ETL pipeline
* Can be scheduled (e.g., daily runs)
* Enables workflow orchestration

---

▶️ How to Run
 1. Clone repository

git clone https://github.com/your-username/job-etl-pipeline.git
cd job-etl-pipeline

2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run pipeline manually

python main.py

5. Run using Airflow

Start Airflow scheduler and webserver, then trigger DAG from UI

 📊 Output

Cleaned job data stored in PostgreSQL and updated via automated pipeline runs.
---

🚀 Future Improvements

* Add logging system
* Implement retry mechanism
* Add data validation
* Build dashboard (Streamlit/Power BI)
  
👨‍💻 Author
Yogesh Singh Mehta
