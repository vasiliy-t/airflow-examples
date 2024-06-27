"""Example DAG demonstrating the usage of the BashOperator."""

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
	dag_id="my_dag_name_3",
	start_date=datetime.datetime(2024, 6, 20),
	schedule="@daily",
):
	EmptyOperator(task_id="task")
