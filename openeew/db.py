from psycopg2 import connect
from os import getenv

_connection = None
db_host = getenv('POSTGRES_SERVICE_HOST','127.0.0.1')
db_port = getenv('POSTGRES_SERVICE_PORT',5432)


def _get_connection():
    global _connection
    if _connection is None:
        _connection = connect(
            user='detector',
            host=db_host,
            port=db_port,
            database='detector'
        )
    return _connection


def execute_statement(statement, parameters):
    connection = _get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(statement, parameters)
        connection.commit()
    except BaseException as exception:
        print(exception)
        connection.rollback()
    finally:
        cursor.close()

