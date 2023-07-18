import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator 
from datetime import datetime, timedelta
from beauty_spider2 import main
from datetime import datetime
current_datetime = datetime.now()
yesterday = current_datetime - timedelta(days=1)
datetime_format = '%Y%m%d'


default_args = {
    'owner': 'jingyu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v07',
    description='Our first dag using python operator',
    start_date=datetime(2023, 7, 17),
    schedule='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='download_beauty_picture',
        python_callable=main
    )
    task2 = BashOperator(
        task_id='delete_yesterday_image_folder',
        bash_command='rm -rf /home/happy_pic/Beauty_PttImg_{:{}}'.format(yesterday, datetime_format)
    )

    task2 >> task1 
