nums = [10, 20, 33, 12, 4, 19, 59, 38, 18, 50, 3]

def line():
	print('-'*50)

def filter_demo(fn):
	# for filter operation fn must be a function or lambda that 
	# takes a single argument and returns bool
	for n in filter(fn, nums): print(n, end=', ')
	print()

def map_demo(fn):
	for n in map(fn, nums): print(n, end=', ')
	print()


def main():

	# filter example
	print('Even numbers : ')
	filter_demo(lambda x: x%2==0)
	line()

	# get all numbers >=30
	print('Numbers >=30 : ')
	filter_demo(lambda x: x>=30)
	line()

	# convert all numbers into it's square
	print("Square of numbers: ")
	map_demo(lambda x: x*x)


if __name__ == '__main__':
	main()








