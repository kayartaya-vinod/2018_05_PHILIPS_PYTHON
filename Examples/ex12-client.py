from socket import *
import json

def main():
	req1 = dict(command='add', args=[12, 34, 56])
	req2 = dict(command='capital', args=['ka'])
	req3 = dict(command='fibonacii', args=[100])
	req4 = dict(command='quit')

	requests = [req1, req2, req3, req4]

	client = socket()
	client.connect((gethostname(), 5000))

	for req in requests:
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