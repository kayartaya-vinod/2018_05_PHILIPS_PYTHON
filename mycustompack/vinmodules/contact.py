class Contact(object):
	def __init__(self, *args, **kwargs):
		self.__id = kwargs.get('id')
		self.__name = kwargs.get('name')
		self.__email = kwargs.get('email')
		self.__phone = kwargs.get('phone')
		self.__city = kwargs.get('city', 'Bangalore')

	@property
	def id(self):
		return id
	@id.setter
	def id(self, id):
		self.__id = id
		
	@property
	def name(self):
		return name
	@name.setter
	def name(self, name):
		self.__name = name
		
	@property
	def email(self):
		return email
	@email.setter
	def email(self, email):
		self.__email = email
		
	@property
	def phone(self):
		return phone
	@phone.setter
	def phone(self, phone):
		self.__phone = phone

	@property
	def city(self):
		return city
	@city.setter
	def city(self, city):
		self.__city = city

	def __getitem__(self, key):
		if key=='id': return self.__id
		if key=='name': return self.__name
		if key=='email': return self.__email
		if key=='city': return self.__city
		if key=='phone': return self.__phone
		

	def __setitem__(self, key, value):
		if key=='id': self.__id = value
		elif key=='name': self.__name = value
		elif key=='email': self.__email = value
		elif key=='city': self.__city = value
		elif key=='phone': self.__phone = value
		
	def __str__(self):
		return 'Contact (id={}, name={}, email={}, phone={}, city={}'.format(
			self.__id, self.__name, self.__email, self.__phone, self.__city )

