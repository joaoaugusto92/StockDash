import mysql.connector
from flask import current_app

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="projetofaculdade",
        user="root",
        password=""
    )
    return conn


