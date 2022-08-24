# Generators are functions that return an iterable collection of items, 
# one at a time, in a set manner. Generators, in general, are used to create 
# iterators with a different approach. 
# They employ the use of yield keyword rather than 
# return to return a generator object.

def fib(n):
   p, q = 0, 1
   while(p < n):
       yield p
       p, q = q, p + q

for i in fib(10):
	print(i)    # output => 0 1 1 2 3 5 8
