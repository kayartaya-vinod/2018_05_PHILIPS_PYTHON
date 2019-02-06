import re
import requests

def main():
	url = 'http://www.gutenberg.org/files/57078/57078-0.txt'
	raw = requests.get(url).text

	start = re.search('1\.', raw).end()
	end = re.search('2\.', raw).start()
	text = raw[start:end].strip()

	with open('1.txt', 'wt') as file:
		file.write(text)

	print('Done.')

if __name__ == '__main__':
	main()
