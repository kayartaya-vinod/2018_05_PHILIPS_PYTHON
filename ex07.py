def main_1():
	# f = open('ex06.py')
	# txt = f.read();
	# f.close()

	# f = open('ex06.py')
	# txt = f.readline();
	# f.close()

	f = open('ex06.py')
	lines = f.readlines();
	f.close()

	print(len(lines))


def main():
	with open('ex06.py') as f:
		i = 1
		for line in f:
			print('{:3}. {}'.format(i, line), end='')
			i+=1

if __name__ == '__main__':
	main()












