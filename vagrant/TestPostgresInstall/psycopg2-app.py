import psycopg2

conn = psycopg2.connect("dbname=db_test user=postgres host=localhost")

conn.close()
