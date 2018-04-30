#Implement functionality of find using find.py?(find.py /root/dirname “txt”)(use sys.argv)

#!/usr/bin/python
import os

def main():
    f = raw_input("Enter the filename: ")
    with open(f, "r")as infile:
        infile.seek(0,2)
        end = infile.tell()
        print(end)
        infile.seek(-end, os.SEEK_END)
        print(infile.readlines()[-1])

if __name__ == "__main__":
    main()
        


