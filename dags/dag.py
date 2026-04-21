# Import required Airflow classes
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Import system libraries to handle file paths
import sys
import os

# Add parent directory to system path
# Taaki hum "scripts" folder ke modules import kar paayein
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import ETL functions from scripts folder
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data


# Main ETL function
def etl_pipeline():
    # Step 1: Extract data from source (API, DB, etc.)
    data = extract_data()
    
    # Step 2: Transform / clean the extracted data
    cleaned = transform_data(data)
    
    # Step 3: Load the cleaned data into destination (DB, warehouse, etc.)
    load_data(cleaned)


# Default arguments for DAG
default_args = {
    # DAG will start running from this date
    "start_date": datetime(2024, 1, 1),
}


# Define the DAG
with DAG(
    dag_id="job_etl_pipeline",        # Unique name for DAG
    default_args=default_args,
    schedule_interval="@daily",      # Runs once every day
    catchup=False                   # Prevents backfilling old runs
) as dag:

    # Define a single task that runs the ETL pipeline
    run_etl = PythonOperator(
        task_id="run_etl",           # Task name in Airflow UI
        python_callable=etl_pipeline # Function to execute
    )

    # Since only one task hai, koi dependency define nahi ki
    # Agar multiple tasks hote toh yaha chaining hoti (>> or <<)
