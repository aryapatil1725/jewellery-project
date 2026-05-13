import pymysql
import os

def get_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'jewellerydb'),
        cursorclass=pymysql.cursors.DictCursor,
        charset="utf8mb4"
    )
