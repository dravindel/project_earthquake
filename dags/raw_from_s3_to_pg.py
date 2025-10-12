import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sensors.external_task import ExternalTaskSensor

# DAG configuration
OWNER = "dravindel"
DAG_ID = "raw_from_s3_to_pg"

# Tables used in the DAG
LAYER = "raw"
SOURCE_TABLE = "earthquake_data"
SCHEMA = "dm"
TARGET_TABLE = "fct_avg_day_earthquake"

#DWH connection
PG_CONNECTION = "pg_dwh"

LONG_DESCRIPTION = """
# LONG DESCRIPTION
"""
SHORT_DESCRIPTION = "SHORT DESCRIPTION"

args = {
    "owner": OWNER,
    "start_date": pendulum.datetime(2025, 1, 1, tz="Europe/Warsaw"),
    "catchup": True,
    "retries": 3,
    "retry_delay": pendulum.duration(hours=1),
}

with DAG(
    dag_id=DAG_ID,
    schedule_interval="0 5 * * *",
    default_args=args,
    tags=["dm", "pg"],
    description=SHORT_DESCRIPTION,
    concurrency=1,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:
    dag.doc_md = LONG_DESCRIPTION

    start = EmptyOperator(
        task_id="start",
    )
