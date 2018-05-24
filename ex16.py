import re

def get_outline():
	with open('outline.txt') as file:
		return file.read()

def get_prerequisites(content):
	pos1 = re.search('Prerequisites:', content).end()
	pos2 = re.search('Software setup:', content).start()
	return content[pos1:pos2]


def main():
	outline = get_outline()
	prerequisites = get_prerequisites(outline)
	print(prerequisites)

if __name__ == '__main__':
	main()