class Queue:
	def __init__(self, max_size):
		self.__max_size = max_size
		self.__elements = [None] * self.__max_size
		self.__rear = 1
		self.__front = 0

	def is_full(self):
		if (self.__rear == self.__max_size - 1):
			return True
		return False

	def is_empty(self):
		if (self.__front > self.__rear):
			return True
		return False

	def enqueue(self, data):
		if (self.is_full()):
			print("Queue is full!!")
		else:
			self.__rear += 1
			self.__elements[self.__rear] = data