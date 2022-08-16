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

	def dequeue(self):
		if (self.is_empty()):
			print("Queue is empty!!")
		else:
			data = self.__elements[self.__front]
			self.__front += 1
			return data

	def display(self):
		for index in range(self.__front, self.__rear + 1):
			print(self.__elements[index])


"""************   Stack     ***********"""

class Stack:
	def __init__(self, max_size):
		self.__max_size = max_size
		self.__elements = [None] * self.__max_size
		self.__top = -1

	def is_full(self):
		if (self.__top == self.__max_size - 1):
			return True
		return False

	def is_empty(self):
		if (self.__top == -1):
			return True 
		return False

	def push(self, data):
		if (self.is_full()):
			print("This stack is full!!")
		else:
			self.__top += 1
			self.__elements[self.__top] = data

	def pop(self):
		if (self.is_empty()):
			print("The stack is empty!!")
		else:
			data = self.__elements[self.__top]
			self.__top -= 1
			return data

	def display(self):
		if (self.is_empty()):
			print("The stack is empty!!")
		else:
			index = self.__top
			while (index >= 0):
				print(self.__elements[index])
				index += 1