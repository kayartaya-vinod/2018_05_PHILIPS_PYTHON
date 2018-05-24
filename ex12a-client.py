from socket import *
import json

def main():
	client = socket()
	client.connect((gethostname(), 5000))
	req = dict(command='get_all_contacts', args=[])


	req = json.dumps(req)
	req = req.encode()
	client.send(req)
	resp = client.recv(1024)
	if resp: 
		resp = str(resp, 'utf-8')
		resp = json.loads(resp)
		print('server response: ', resp)

	client.close()

if __name__ == '__main__':
	main()