#read file from different directory

#!/usr/bin/python
import os

def main():
    f = raw_input("Enter file :")
    for roots,dirnames,file_names in os.walk("/"):
        for files in file_names:
            if files == f:
                file_path = os.path.join(r,files)
                with open(file_path, "r") as infile:
                    for line in infile:
                        print line

if __name__ == "__main__":
    main()
