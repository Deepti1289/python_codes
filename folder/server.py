#!/usr/bin/python

import socket
import sys
import threading
import subprocess
import argparse

def SendRecv(connection, client_address):
    try:
        print("connection from, connection is ", client_address, connection)
        cmd = connection.recv(2)
        data = subprocess.check_output(cmd)
        if data:
            print("sending data back to client")
            connection.sendall(data)
        else:
            print("no more data")
    finally:
        connection.close()
     

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str, help="server ip address")
parser.add_argument("-p", type=int, help="port number of server")
args = parser.parse_args()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket to the port
server_address = (args.s, args.p)
print("starting up on %s port %s" %server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    #wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    SendRecv(connection,client_address)    
