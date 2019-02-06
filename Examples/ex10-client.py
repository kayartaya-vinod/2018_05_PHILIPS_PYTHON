from socket import *

def main():
	client = socket()
	addr = (gethostname(), 5000)
	client.connect(addr)

	message = input('Enter message to send: ')

	client.send(message.encode())

	serv_message = client.recv(1024)
	serv_message = str(serv_message, 'utf-8')

	client.close()

	print('Reply from server: ', serv_message)

if __name__ == '__main__':
	main()