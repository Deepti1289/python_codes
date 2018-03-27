#!/usr/bin/python

import subprocess
import time
import sys
import signal

def parsing(filename,filename_result):
    tps_avg = 0
    reads_avg = 0
    writes_avg = 0
    read_avg = 0
    write_avg = 0
    count = 0
    with open(filename,"r") as infile:
        next(infile)
        for line in infile:
            device, tps, reads, writes, read, write = line.split()
            count += 1
            tps_avg += float(tps)
            reads_avg += float(reads)
            writes_avg += float(writes)
            read_avg += float(read)
            write_avg += float(write)
    tps_avg = tps_avg/count
    reads_avg = reads_avg/count
    writes_avg = writes_avg/count
    read_avg = read_avg/count
    write_avg = write_avg/count
    with open(filename_result,"a") as result_file:
        result_file.write(str(tps_avg)+" "+str(reads_avg)+" "+str(writes_avg)+" "+str(read_avg)+" "+str(write_avg))

def print_stats(filename,name):
    try:
        filename_result = filename+"_"+"result"
        with open(filename,"a") as infile:
            infile.write("Devices" +"       "+"tps"+"    "+"KB_read/s"+"    "+"KB_read"+"    "+"KB_write"+"\n")
        cmd = "iostat -d 1"
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in iter(output.stdout.readline, ""):
            if name in line:
                with open(filename,"a") as outfile:
                    outfile.write(line)

    except:
        print("exception")
    finally:
        print("Program Completed")
        print("Waiting for parsing the result .........")
        parsing(filename,filename_result)
        sys.exit(0)

while True:
    print("Enter the device: ")
    name = raw_input()
    timetoday = time.strftime("%H%M%S_%d%m%y")
    filename = name+"_"+timetoday
    print_stats(filename,name)
