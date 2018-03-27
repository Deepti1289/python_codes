#!/usr/bin/python

import threading
import sys
import argparse
import ConfigParser
import socket
import sys
import string

class Client(threading.Thread):
    def __init__(self,port,ip,status_command,output_file):
        threading.Thread.__init__(self)
        #port,ip,status_command,output_file = args.split(",")
        self.port = int(port)
        self.ip = ip
        self.status_command = status_command
        self.output_file = output_file
        print(self.port)

    def run(self):
        BUFF_SIZE = 4096
        #Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Connect the socket to the port where the server is listening
        server_address = (self.ip, self.port)
        print("connecting to %s port %s" % server_address)
        sock.connect(server_address)

        try:
            sock.sendall(self.status_command)
            data = sock.recv(BUFF_SIZE)
            with open(self.output_file,"a") as infile:
                infile.write(data)
        finally:
            print("closing socket")
            sock.close()

def open_file(filename,config):
    my_list = []
    c_list = []
    with open(filename, "r") as infile:
        config.read(filename)
        for server in config.sections():
            my_list.append((int(config.get(server, "port")),config.get(server, "ip"),config.get(server, "status_command"),config.get(server, "output_file")))
    for i in range(0,len(my_list)): 
         c_list.append(Client(*my_list[i]))

    print(c_list)
    for client in c_list:
        client.start()
    
   
        
def main():
    config = ConfigParser.ConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="input a file")
    args = parser.parse_args()
    open_file(args.f,config)

if __name__ =="__main__":
    main()
