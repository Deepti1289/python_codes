#!/usr/bin/python


def divisibleby(x):
    return x%2 == 0 and x%3 == 0

print (filter(divisibleby, range(2,25)))
