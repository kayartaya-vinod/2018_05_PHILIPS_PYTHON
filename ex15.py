import threading
import time

class SentenceToWords(threading.Thread):

	def __init__(self, sentence, words):
		super().__init__()
		self.__sentence = sentence 		# str
		self.__words = words			# list, shared

	def run(self):
		lst = self.__sentence.split(' ')
		lk = threading.Lock()
		lk.acquire()
		for word in lst:
			self.__words.append(word)
		lk.release()

def main():
	words = []
	s1 = 'my name is vinod and i live in bangalore'
	s2 = 'quick brown fox jumped over lazy dog'

	t1 = SentenceToWords(s1, words)
	t2 = SentenceToWords(s2, words)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	sentence = ' '.join(words)
	print(sentence)

if __name__ == '__main__':
	main()







