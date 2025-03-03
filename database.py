import os 
import json 
import mysql.connector as sql
import bcrypt
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
    'port': int(os.getenv('DB_PORT'))
}

try:
    connection = sql.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute('SELECT DATABASE()')
    row = cursor.fetchone()
    print('Connected to database',)
    connection.close()   
except Exception as e:
    print('Error to conect to database', e)


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def InsertInTableUsers(data):
    try:
        connection = sql.connect(**DB_CONFIG)   
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (username, password, birth_date, email) VALUES (%s, %s, %s, %s)', data)
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print('Error to insert in table', e)
        return False


