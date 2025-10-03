import mysql.connector
import pandas as pd

def conexao (query):

    conn = mysql.connector.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'root',
        password = 'Senai@134',
        db = 'db_projeto'
    )

    dataframe = pd.read_sql(query, conn)
    conn.close()

    return dataframe