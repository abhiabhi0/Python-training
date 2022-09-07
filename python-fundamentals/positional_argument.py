def foo(a, b, c=None, d=None, *args, **kwargs):
    print(a,b,c,d)

foo(1,2,3,4) # o/p = 1 2 3 4
foo(1, 2, 3,4, 5, 6) # o/p = 1, 2, 3, 4
foo(1, 2, 3, c=4) # error TypeError: foo() got multiple values for argument 'c'

  