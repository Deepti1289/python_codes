#Traverse each file of a directory and print last line of each file

#!/usr/bin/python
import os

def find_dir():
    my_list = []
    my_dir = raw_input("Enter the directory name that you want to traverse: ")
    for roots,dirnames,filenames in os.walk(my_dir):
        for files in filenames:
            my_list.append(os.path.join(roots,files))
            #print(my_list)
    return my_list

def read_last_line(my_list):
    for file in my_list:
        with open(file, "r") as infile:
            infile.seek(0,2)
            end = infile.tell()
            infile.seek(-end, 2)
            print(infile.readlines()[-1])
        
def main():
    my_list = find_dir()
    print(my_list)
    read_last_line(my_list)
    
    
if __name__ == "__main__":
    main()
    
