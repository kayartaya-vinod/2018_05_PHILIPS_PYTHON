import pymysql

def get_connection():
	dbprops = {}
	dbprops['database'] = 'training'
	dbprops['host'] = 'localhost'
	dbprops['user'] = 'root'
	dbprops['password'] = 'root'
	dbprops['port'] = 3306

	return pymysql.connect(**dbprops)

def main():
	conn = get_connection()
	print(conn)

if __name__ == '__main__':
	main()