#!/usr/bin/python

def Increament(n):
    return lambda x:x+n

increament_by_5 = Increament(5)
increament_by_10 = Increament(10)
increament_by_100 = Increament(100)
print(increament_by_5(1))
print(increament_by_100(1))
print(increament_by_10(2))
