import mysql.connector as msql
from mysql.connector import Error


def cria_db_conex():
    try:
        conn = msql.connect(host = '192.168.0.35', user = 'root', password = 'mysql_321654')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS db')
            #print('Banco de dados criado!)
                    
    except Error as e:
        print('Erro ao tentar conectar ao banco', e)

cria_db_conex()
