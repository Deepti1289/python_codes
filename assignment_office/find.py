#Implement functionality of find using find.py?(find.py /root/dirname “txt”)(use sys.argv)

#!/usr/bin/python
import os
import sys
import fnmatch

def find_file(path,my_file):
    result = []
    for roots,dirnames,filenames in os.walk(path):
        for file in filenames:
            if file.endswith(my_file):
                result.append(os.path.join(roots,file))
    return result

def main():
    path = sys.argv[1]
    my_file = sys.argv[2]
    print(find_file(path, my_file))

if __name__ == "__main__":
    main()
