#!/usr/bin/python

import sys
import argparse
import ConfigParser
import socket
import sys
import string


def open_file(filename,config):
    with open(filename, "r") as infile:
        config.read(filename)
        for server in config.sections():
            print(config.get(server, "port"))
            #print(port)
            print(config.get(server, "ip"))
            print(config.get(server, "status_command"))
            print(config.get(server, "output_file"))
            client(int(config.get(server, "port")),config.get(server, "ip"),config.get(server, "status_command"),config.get(server, "output_file"))

def client(port,ip,status_command,output_file):
    BUFF_SIZE = 4096
    #Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print("connecting to %s port %s" % server_address)
    sock.connect(server_address)

    try:
        sock.sendall(status_command)
        data = sock.recv(BUFF_SIZE)
        with open(output_file,"a") as infile:
            infile.write(data)
    finally:
        print("closing socket")
        sock.close()


        
def main():
    config = ConfigParser.ConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="input a file")
    args = parser.parse_args()
    open_file(args.f,config)

if __name__ =="__main__":
    main()
