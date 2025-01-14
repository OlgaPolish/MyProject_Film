import pymysql
from pymysql.err import MySQLError
import os
from dotenv import load_dotenv

load_dotenv()

# ------------- Database Configurations -------------
DB_CONFIG_QUERY = {
    'host': os.getenv('DB_QUERY_HOST'),
    'user': os.getenv('DB_QUERY_USER'),
    'password': os.getenv('DB_QUERY_PASSWORD'),
    'database': os.getenv('DB_QUERY_NAME')
}

DB_CONFIG_WRITE = {
    'host': os.getenv('DB_WRITE_HOST'),
    'user': os.getenv('DB_WRITE_USER'),
    'password': os.getenv('DB_WRITE_PASSWORD'),
    'database': os.getenv('DB_WRITE_NAME')
}

# ------------- Database Connections -------------
def create_connection_mysql_db_query():
    try:
        connection_query = pymysql.connect(**DB_CONFIG_QUERY)
        return connection_query
    except MySQLError as e:
        raise MySQLError(f"Error connecting to MySQL Platform (Query DB): {e}")


def create_connection_mysql_db_write():
    try:
        connection_write = pymysql.connect(**DB_CONFIG_WRITE)
        return connection_write
    except MySQLError as e:
        raise MySQLError(f"Error connecting to MySQL Platform (Write DB): {e}")
