import threading
import time
import random

import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Receive data from the server
    data_from_server=cs.recv(200)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # Open file to read from
    while True:
        read_file = open('in-proj.txt', 'r')
        for line in read_file:
            cs.send(str(line).encode('utf-8'))
            time.sleep(2)
        read_file.close()

        # close the client socket
        cs.close()
        exit()

if __name__ == "__main__":
    client()