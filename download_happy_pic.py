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
    dag_id='my_scheduler_to_download_happy_pic',
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
    task3 = BashOperator(               
        task_id='delete_announce_image_folder',
        bash_command='find /home/happy_pic/Beauty_PttImg_20230719 -type d -name "*檢舉建議專區*" -exec rm -rf {} +'
    )
    task2 >> task1 >> task3
