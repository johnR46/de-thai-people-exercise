import datetime

from airflow.decorators import dag
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.utils.helpers import chain


@dag(start_date=datetime.datetime(2024, 1, 1), schedule=None)
def thai_people_exercise_dag():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    @task()
    def download_dataset_task():
        pass

    @task()
    def upload_to_bucket_task():
        pass

    @task()
    def pyspark_task():
        pass

    t1 = download_dataset_task()
    t2 = upload_to_bucket_task()
    t3 = pyspark_task()

    chain(
        start,
        t1,
        t2,
        t3,
        end
    )


thai_people_exercise_dag()
