#!/usr/bin/python

def Square(x):
    return x*x

x = map(Square, range(1,30,2))
#x = map(lambda x: x*x, range(1,30,2))
print(x)
