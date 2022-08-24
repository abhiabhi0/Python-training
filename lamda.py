mul = lambda a, b : a * b
print(mul(2, 5))

def myWrapper(n):
	return lambda a : a * n

mulFive = myWrapper(5)
print(mulFive(2))