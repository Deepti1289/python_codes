#!/usr/bin/python

def swap_case(s):
    new_string = ""
    for item in s:
        if item.isupper():
            new_string += item.lower()
        else:
            new_string += item.upper()
    return new_string

def main():
    s = raw_input("Input string :")
    print(swap_case(s))

if __name__ == "__main__":
    main()
