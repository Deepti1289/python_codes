#!/usr/bin/python

def char_count(my_str):
    count = 1
    max_count = 1
    max_word = ""
    for i in range(1,len(my_str)):
        if ((my_str[i-1]) == my_str[i]):
            count += 1
        else:
            if (count > max_count):
                max_count = count
                max_word = my_str[i-1]
            count = 1
    if(count > max_count):
        max_count = count
        max_word = my_str[i-1]
    return max_word

def main():
    my_str = raw_input("Input the string :")
    print(char_count(my_str))

if __name__ == "__main__":
    main()
