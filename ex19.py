import re
import requests

def main():
	url = 'test.html'
	with open('test.html', 'rt') as file:
		raw = file.read()
		print(raw)
		match = re.search('<a.*?</a>', raw)

		x = 1
		while match is not None:
			print(match.group())
			index = match.end()
			match = re.search('<a.*?</a>', raw[index+1:])
			x += 1
			if x>10: break


if __name__ == '__main__':
	main()