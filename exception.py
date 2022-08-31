def divideNos(a, b):
  return a/b # An exception might raise here if b is 0 (ZeroDivisionError)
try:
   a = input('enter a:')
   b = input('enter b:')
   print('after division', divideNos(a, b)) 
   a = [1, 2, 3]
   print(a[3]) # An exception will raise here as size of array ‘a’ is 3 hence is accessible only up until 2nd index
 
# if IndexError exception is raised
except IndexError:            
   print('index error')
# if ZeroDivisionError exception is raised
except ZeroDivisionError:
   print('zero division error')

#Ex 2
def divideNos(a, b):
 return a/b
try:
 a = int(input('enter a:'))
 b = int(input('enter b:'))
 print('after division', divideNos(a,b))
 a = [1, 2, 3]
 print(a[3])
except (IndexError, ZeroDivisionError):
  print('index error OR zero division error')


#Custom Exception

def divideNos(a, b):
 return a/b
try:
 a = int(input('enter a:'))
 b = int(input('enter b:'))
 print('after division', divideNos(a,b))
 a = [1, 2, 3]
 print(a[3])
except (IndexError, ZeroDivisionError):
  print('index error OR zero division error')

  #else clause example

  try:
   b  = 10
   c = 0
   a = b/c
   print(a)
except Exception as e:
   print('Exception raised:', e)
else:
   print('no exceptions raised')


# Try Clause with Finally

try:
 temp = [1, 2, 3]
 temp[4]
except Exception as e:
 print('in exception block: ', e)
else:
 print('in else block')
finally:
 print('in finally block')
