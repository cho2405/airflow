from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.slack_operator import SlackAPIPostOperator


start_date = datetime.combine(datetime.today(), datetime.min.time())
default_args = {
    'owner': 'hana',
    'depends_on_past': False,
    #'start_date': airflow.utils.dates.days_ago(2),
    'start_date': start_date
}

dag = DAG(
    dag_id='test_slack',
    default_args=default_args,
    schedule_interval='0 1 * * 1-5',
)

t1 = SlackAPIPostOperator(
    task_id='send_slack',
    token='xoxb-1047699065494-1896795313409-8of6dtvIUyV18tYsAnXv7Obc',
    channel='#data_analysis',
    username='tester',
    text='출근합시다! \n',
    dag=dag 
)


