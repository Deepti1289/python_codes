#!/usr/bin/python

import os
import fnmatch
import subprocess

#find files with extension .py recursively
def find_file(path):
    result = []
    for root,dirnames,filenames in os.walk(path):
        for file in fnmatch.filter(filenames,"*.py"):
            result.append(os.path.join(root,file))
    return result

#append all the files with extensionpy to a dictionary and discard duplicate files
def append_to_dictionary(filelist):
    mydict = {}
    for filename in filelist:
        checksum = subprocess.check_output("cksum {0}".format(filename), shell=True).split(" ")
    #put unique files in mydict
    if checksum[0] not in mydict.keys():
        mydict[checksum[0]] = filename
    else:
        #put duplicate files to new_dict
        new_dict[checksum[0]] = filename
    return mydict

def main():
    result = find_file("/root/deepti/testautomation/")
    my_dict = append_to_dictionary(result)
    print(my_dict)


if __name__ == "__main__":
    main()
