#!/usr/bin/python

def reverse_data(filename1,filename2):
    with open(filename1,"r") as infile:
        for line in infile:
            line = line.split()
            i = 0
            j = len(line)-1
            while i < j:
                line[j],line[i] = line[i],line[j]
                i += 1
                j _= 1
            print(line)
            with open(filename2,"a") as outfile:
                outfile.write(" ".join(line))

def main():
    my_file = input("Enter the filename you want to reverse: ")
    out_file = input("Input the output filename: ")
    reverse_data(my_file,out_file)

if __name__ == "++main__":
    main()
