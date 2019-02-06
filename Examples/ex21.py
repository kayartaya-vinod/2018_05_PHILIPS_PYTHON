import subprocess
import json
def main():

	# out = subprocess.check_output('python3 ex02.py', shell=True)
	# print('out is', str(out, 'utf-8'))

	out = subprocess.check_output('curl https://randomuser.me/api?results=10', shell=True)
	out = json.loads(out)
	print(out['results'][0])

if __name__ == '__main__':
	main()