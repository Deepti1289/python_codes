#!/usr/bin/python

def adder(no):
    def add(number):
        return no+number
    return add

adder_10 = adder(10)
print(adder_10(100))
print(adder_10(25))
