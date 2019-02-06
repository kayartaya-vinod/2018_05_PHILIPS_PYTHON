from socket import *

def main():
	server = socket(AF_INET, SOCK_STREAM) 
	addr = (gethostname(), 5000)
	server.bind(addr)
	server.listen()

	print('server stared at: ', addr)
	while True:
		client, cl_addr = server.accept()
		print('Got a connection from', cl_addr)
		input = client.recv(1024)

		input = str(input, encoding='utf-8')
		print('input from client:', input)

		client.send(input.upper().encode())
		client.close()

if __name__ == '__main__':
	main()