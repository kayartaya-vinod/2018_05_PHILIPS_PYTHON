from socket import *
import json
import threading

class MethodInvoker(threading.Thread):
	def __init__(self, client):
		threading.Thread.__init__(self)
		self.__client = client

	def run(self):
		functions = dict(add=add, capital=capital)
		while True:
			req = self.__client.recv(1024)
			req = str(req, 'utf-8') # bytes to str
			req = json.loads(req) # str to python type (dict in this case)
			if req['command'] =='quit': break

			resp = {}

			if req['command'] in functions:
				resp['success'] = True
				resp['data'] = functions.get(req['command'])(*req['args'])
			else:
				resp['success'] = False
				resp['message'] = 'unknown command'

			resp = json.dumps(resp) # dict to str
			resp = resp.encode() # str to bytes
			self.__client.send(resp)

		self.__client.close()
		print('client connection closed')



def add(*args):
	return sum([a for a in args if type(a) in (int, float)])

def capital(state):
	states = dict(ka='bangalore', tn='chennai', mh='mumbai')
	return states.get(state, 'no data')

# functions = {}
# functions['add'] = add
# functions['capital'] = capital
functions = dict(add=add, capital=capital)

def main():
	server = socket()
	server.bind((gethostname(), 5000))
	server.listen()
	print('server started')

	while True:
		client, cl_addr = server.accept() # get one client connection
		MethodInvoker(client).start()


if __name__ == '__main__':
	main()




