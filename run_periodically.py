#!/usr/bin/python

import subprocess
import time

'''def main():
    count = 0
    while count != 10:
        time.sleep(5)
        proc = subprocess.Popen(["ps", "-A"], shell=True)
        proc.communicate()[0]
        count += 1
   '''

def main():
    count = 0
    while count != 10:
        time.sleep(5)
        cmd = "top -n 1"
        proc = subprocess.Popen(cmd, shell=True)
        proc.communicate()[0]
        count += 1 

if __name__ == "__main__":
    main()
