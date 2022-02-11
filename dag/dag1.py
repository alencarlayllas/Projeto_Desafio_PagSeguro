from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
import mysql.connector as msql
from mysql.connector import Error
from cria_database import cria_db_conex
from cria_nova_tabela import criando_tabela_testando
from limpa_dados import tratando_os_dados

#INICIANDO A DAG:

#PARAMETROS PADRÕES:

args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 30),
    'email': ['alencarlayllas@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=30),
    'scheduler_inteval':'*/15****'    
}

with DAG(
    'dados_kaggle_pgs_etl',
    default_args = args,
    schedule_interval= timedelta(minutes= 1),
    catchup = False,
    tags=['desafio_pagseguro'],
) as dag:
    
    t1 = BashOperator(
    task_id= 'Criando_DB',
    bash_command= cria_db_conex,
    dag = dag 
    )
    
    t2 = BashOperator(
    task_id= 'Criando_Tabela_e_Inserindo_dados_tratados',
    bash_command= criando_tabela_testando,
    dag = dag 
    )
    
    t1 >> t2