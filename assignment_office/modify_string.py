#Ques: WAP to modify a string?(Hello Python)
#OUTPUT: Hello jython
#!/usr/bin/python

str = "Hello Python"
list1 = list(str)
list1[6] = "J"
str = "".join(list1)
print(str)
