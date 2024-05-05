import datetime

from airflow.decorators import dag
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.utils.helpers import chain


@dag(start_date=datetime.datetime(2024, 1, 1), schedule=None)
def word_count():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    @task()
    def pyspark_task():
        pass

    t1 = pyspark_task()

    chain(
        start,
        t1,
        end
    )


word_count()
