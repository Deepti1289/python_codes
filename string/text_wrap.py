#!/usr/bin/python

def wrap(my_str,max_width):
    i = 0
    my_list = []
    while (i <= len(my_str)):
        my_list.append(my_str[i:i+max_width])
        i += max_width
    my_str = "\n".join(my_list)
    return my_str

if __name__ == "__main__":
    my_str = raw_input("Enter the string")
    max_width = int(raw_input("Enter the width"))
    result = wrap(my_str,max_width)
    print(result)
