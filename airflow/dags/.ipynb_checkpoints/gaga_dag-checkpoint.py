import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG(dag_id='gaga_dag', schedule_interval=None)

task = BashOperator(
    task_id='sleeps_forever',
    dag=dag,
    bash_command="sleep 7",
    start_date=airflow.utils.dates.days_ago(2),
    owner='airflow',
)