
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


from airflow.utils.dates import days_ago, infer_time_unit

default_args = {
    'owner': 'Maycon Batestin',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    
}

api = DAG('MONGO',default_args=default_args, tags=["python", "dados", "apis", "pipeline"], description='Pipeline para processamento de dados para o banco de dados MONGODB', schedule_interval=None, catchup=False)


cavaleirodoszodiacos = BashOperator(
    task_id='Cavaleirozodiacos',
	bash_command='python /usr/local/airflow/mongo/scripts/cavaleirodoszodiacos/load.py',
    dag=api
)

disney = BashOperator(
    task_id='disney',
	bash_command='python /usr/local/airflow/mongo/scripts/disney/load.py',
    dag=api
)

futurama = BashOperator(
    task_id='futurama',
	bash_command='python /usr/local/airflow/mongo/scripts/futurama/load.py',
    dag=api
)

gameofthrones = BashOperator(
    task_id='Gamethrones',
	bash_command='python /usr/local/airflow/mongo/scripts/gameofthrones/load.py',
    dag=api
)

pokemon = BashOperator(
    task_id='Pokemon',
	bash_command='python /usr/local/airflow/mongo/scripts/pokemon/load.py',
    dag=api
)

rickandmorty = BashOperator(
    task_id='Rickmorty',
	bash_command='python /usr/local/airflow/mongo/scripts/rickandmorty/load.py',
    dag=api
)

starwars= BashOperator(
    task_id='Starwars',
	bash_command='python /usr/local/airflow/mongo/scripts/starwars/load.py',
    dag=api
)

cavaleirodoszodiacos >> disney >> futurama >> gameofthrones >> starwars >> pokemon >> rickandmorty