#!/usr/bin/python


def read_file(file_name):
    my_dict = {}
    with open(file_name, "r") as infile:
        next(infile)
        for line in infile:
            line = line.split()
            line[1] = int(line[1][:-1])
            print(line)
            my_dict[line[0]] = line[1]
    return my_dict

def find_min(my_dict):
    value = min(my_dict.values())
    for k in my_dict.keys():
        if my_dict[k] == value:
            print(k, my_dict[k]) 
    
    #print(min(my_dict.items(), key=lambda x: x[1]))

def main():
    file_name = raw_input("Enter the file name")
    my_dict = read_file(file_name)
    find_min(my_dict)

if __name__ == "__main__":
    main()
