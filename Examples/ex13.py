import threading
import time

class Fibo(threading.Thread):
	def __init__(self, num):
		super().__init__()
		self.__num = num

	def run(self):
		print('a Fibo thread is started')
		a, b = -1, 1
		for i in range(0, self.__num):
			c = a + b
			print(c)
			time.sleep(1)
			a = b
			b = c

def main():
	print('start of main thread')

	f = Fibo(1500)
	f.setDaemon(True)
	f.start()
	
	for i in range(1, 5):
		time.sleep(1)
		print('in main, i is', i)

	print('end of main thread')


if __name__ == '__main__':
	main()





