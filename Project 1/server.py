import threading
import time
import random

import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    # Open files to write to
    write_in = open('out-proj.txt', 'w')
    write_rev = open('outr-proj.txt', 'w')
    write_upper = open('outup-proj.txt', 'w')

    # send a intro message to the client.
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))


    while True:
        data = csockid.recv(200)
        if data == '':
            write_rev.close()
            print('Done.')
            # close the server socket
            ss.close()
            exit()
        else:
            # Reverse and uppercase the string
            reversedString = data.rstrip()[::-1]
            upperString = data.upper()
            write_in.write(data)
            write_rev.write(reversedString + '\n')
            write_upper.write(upperString)

if __name__ == "__main__":
    server()