from ex02 import Product

def main():
	laptops = [
		Product(name='Lenovo', price=45000),
		Product(name='Aceer', price=42000),
		Product(name='Toshiba', price=15000),
		Product(name='Apple', price=105000),
		Product(name='Dell', price=75000) ]

	from functools import reduce

	total_cost = reduce(lambda x, y: x+y, [lt.price for lt in laptops])
	print('Total cost of all laptops = ', total_cost)

	laptop_names = [ lt.name for lt in laptops ]
	laptop_prices = [ lt.price for lt in laptops ]
	laptop_info = [ (lt.name, lt.price) for lt in laptops ]

	costly_laptops = [ lt.name for lt in laptops if lt.price>=50000 ]

	print(laptop_names)
	print(laptop_prices)
	print(laptop_info)
	print(costly_laptops)

	print('-'*50)


	for laptop in sorted(laptops, reverse=True):
		print(laptop)

	print('-'*50)

	for laptop in sorted(laptops, key = lambda p: p['name']):
		print(laptop)

	



if __name__ == '__main__':
	main()