#!/usr/bin/python

def multiply(x,y):
    return x*y

result = reduce(multiply, range(1,10))
print(result)
