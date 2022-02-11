import mysql.connector as msql
from mysql.connector import Error
from limpa_dados import df


def criando_tabela_testando():
    try: 
        conn = msql.connect(host = '192.168.0.35', user = 'root', database = 'db', password = 'mysql_321654')
        
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('select database()')
            record = cursor.fetchone()
            print("Conectado ao banco de dados: ", record)
            cursor.execute('DROP TABLE IF EXISTS transactions')
            cursor.execute('CREATE TABLE IF NOT EXISTS db.transactions(id INT, step INT, customer VARCHAR(50), age VARCHAR(50), \
            gender VARCHAR(50), zipcodeOri VARCHAR(50), merchant VARCHAR(50), zipMerchant VARCHAR(50),\
            category VARCHAR(50),amount FLOAT, fraud INT, year INT, month INT, day INT)')       
            print('Table is created')
            
            for i, row in df.iterrows():
                sql = 'INSERT INTO db.transactions (id, step, customer, age, gender, zipcodeOri, merchant, zipMerchant, category, amount, fraud, year, month, day) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)'
                cursor.execute(sql, tuple(row))
                print('Dado Inserido')
                conn.commit()
            
    except Error as e:
        print('Erro ao tentar conectar ao banco', e)

criando_tabela_testando()
