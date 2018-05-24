from mysql.connector import MySQLConnection as connect

mysql_info = {}
mysql_info['host'] = 'localhost'
mysql_info['port'] = '3306'
mysql_info['database'] = 'training'
mysql_info['user'] = 'root'
mysql_info['password'] = 'root'

# from psycopg2 import connect
pg_info = {}
pg_info['host'] = 'localhost'
pg_info['port'] = '5432'
pg_info['database'] = 'training'
pg_info['user'] = 'postgres'
pg_info['password'] = ''

db_info = mysql_info
# db_info = pg_info

conn = connect(**db_info)
cur = conn.cursor()

cur.execute('select * from contacts')
data = cur.fetchall()
for d in data:
	print(d)

cur.close()
conn.close()











