class Product(object):

	__id_counter = 0

	def __init__(self, **kwargs):
		Product.__id_counter += 1
		self.__id = Product.__id_counter
		self.__name = kwargs.get('name')
		self.__price = kwargs.get('price')
		self.__category = kwargs.get('category', 'computers')

	def __str__(self):
		return 'Product [id={}, name={}, price={}, category={}]'.format(
			self.__id, self.__name, self.__price, self.__category)

	# expose a private attribute as a public read-only property
W

	@property
	def name(self):
		return self.__name

	# writable (settable) property for 'name'
	@name.setter
	def name(self, value):
		if type(value) != str:
			raise TypeError('Only strings can be assigned')
		elif value.strip()=='':
			raise ValueError('Empty string not allowed')

		self.__name = value

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		if type(value) not in (int, float):
			raise TypeError('Only numbers can be assigned')
		elif value < 0:
			raise ValueError('Price must be >= zero')

		self.__price = value

	@property
	def category(self):
		return self.__category.upper()

	@category.setter
	def category(self, value):
		if type(value) != str:
			raise TypeError('Only strings can be assigned')
		elif value.strip()=='':
			raise ValueError('Empty string not allowed')

		self.__category = value

	def __getitem__(self, key):
		if key not in ('id', 'name', 'price', 'category'):
			raise KeyError('Invalid key. Use one of: id, name, price, category')

		if key=='id': 
			return self.__id
		elif key=='name':
			return self.__name
		elif key=='price':
			return self.__price
		elif key=='category':
			return self.__category

	def __setitem__(self, key, value):
		if key not in ('name', 'price', 'category'):
			raise KeyError('Invalid key. Use one of: name, price, category')
		
		if key=='name':
			self.__name = value
		elif key=='price':
			self.__price = value
		elif key=='category':
			self.__category = value

	def __lt__(self, other):
		if type(other) != Product:
			raise TypeError('Invalid type for < comparison')

		return self.__price < other.__price

	# def __le__(self, other):
	# 	if type(other) != Product:
	# 		raise TypeError('Invalid type for <= comparison')

	# 	return self.__price <= other.__price

	# def __gt__(self, other):
	# 	if type(other) != Product:
	# 		raise TypeError('Invalid type for > comparison')

	# 	return self.__price > other.__price

	# def __ge__(self, other):
	# 	if type(other) != Product:
	# 		raise TypeError('Invalid type for >= comparison')

	# 	return self.__price >= other.__price

def main():
	p1 = Product(name='Apple macbook pro', price=108000)
	p2 = Product(name='Lenovo Z650', category='computers', price=45000)

	p1['category'] = 'Computers***'

	print("p1['id']", p1['id'])
	print("p1['name']", p1['name'])
	print("p1['price']", p1['price'])
	print("p1['category']", p1['category'])

	p2.__price = 55000 # does not change the member attribute

	print(p1) # invokes p1.__str__() implicitly
	print(p2)

	p1.name = 'Apple McBook Pro'
	p1.category = 'laptops'
	p1.price -= 3000

	print('p1.id is', p1.id)
	print('p1.name is', p1.name)
	print('p1.price is', p1.price)
	print('p1.category is', p1.category)

if __name__ == '__main__':
	main()


