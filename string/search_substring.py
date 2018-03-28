#!/usr/bin/python

import re

my_str = raw_input("Input string :")
sub_str = raw_input("Input string :")
x = re.search(sub_str,my_str)
i = 0
if not x:
    print(-1,-1)
while x!= None:
    print((x.start()+i, x.end()-1+i))
    i += x.start()+1
    my_str = my_str[x.start()+1:]
    x = re.search(sub_str,my_str)
