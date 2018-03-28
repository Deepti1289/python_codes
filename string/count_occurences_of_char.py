#!/usr/bin/python

def count_occur(my_str):
    count = 1
    new_str = ""
    for i in range(1,len(my_str)):
        if (my_str[i-1] == my_str[i]):
            count += 1
        else:
            new_str += my_str[i-1] + str(count)
            count = 1
    new_str += my_str[i] + str(count)
    return new_str
         

def main():
    my_str = raw_input("Enter the string")
    print(count_occur(my_str))

if __name__ == "__main__":
    main()
