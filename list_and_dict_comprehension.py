my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]    # list comprehension

squared_dict = {x:x**2 for x in my_list}    # dict comprehension

squared_list = [x**2 for x in my_list if x%2 != 0]    # list comprehension

squared_dict = {x:x**2 for x in my_list if x%2 != 0}    # dict comprehension

a = [1, 2, 3]
b = [7, 8, 9]

[(x + y) for (x,y) in zip(a,b)]  # parallel iterators

[(x,y) for x in a for y in b]    # nested iterators

my_list = [[10,20,30],[40,50,60],[70,80,90]]
flattened = [x for temp in my_list for x in temp]
