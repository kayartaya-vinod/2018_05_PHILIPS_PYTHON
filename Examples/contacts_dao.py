import pymysql
from contact import Contact

def get_connection():
	dbprops = {}
	dbprops['database'] = 'training'
	dbprops['host'] = 'localhost'
	dbprops['user'] = 'root'
	dbprops['password'] = 'root'
	dbprops['port'] = 3306

	return pymysql.connect(**dbprops)


def get_contact(t):
	if t==None: return None

	c = Contact()
	c.id = t[0]
	c.name = t[1]
	c.email = t[2]
	c.phone = t[3]
	c.city = t[4]
	return c

def get_all_contacts():
	conn = get_connection()
	cur = conn.cursor()
	cur.execute('select * from contacts')

	return [ get_contact(rec) for rec in cur.fetchall()]

def get_one_contact(id):
	conn = get_connection()
	cur = conn.cursor()
	cur.execute('select * from contacts where id=%s', (id,))

	return get_contact(cur.fetchone())


def main():
	# contacts = get_all_contacts()
	# for c in contacts:
	# 	print(c)

	contact = get_one_contact(1)
	print(contact)


if __name__ == '__main__':
	main()



