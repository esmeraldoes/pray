from django.db import connection

def delete_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

delete_table('')
