import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="00000000",
        database="matricula",
        port=3306,
        connection_timeout=30
    )
