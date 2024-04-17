import select
import socket
import sys

def ls(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: LS Socket Created")
        ts1Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: TS1 Socket Created")
        ts2Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: TS2 Socket Created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    host = socket.gethostname()
    server_binding = ("", lsListenPort)
    print("[S]: LS Server host name is {}".format(host))
    ss.bind(server_binding)
    ss.listen(5)
    csockid, add = ss.accept()

    ts1Socket.connect((ts1Hostname, ts1ListenPort))
    ts2Socket.connect((ts2Hostname, ts2ListenPort))

    inputs = [ts1Socket, ts2Socket]
    outputs = []

    while True:
        data = csockid.recv(200).decode('utf-8').strip()
        ts1Socket.send(data)
        ts2Socket.send(data)
        readable, writable, exceptional = select.select(inputs, outputs, [], 5)

        if readable:
            data_from_ts = readable[0].recv(200).decode('utf-8')
            try:
                csockid.send(data_from_ts)
            except socket.error as err:
                print('[S]: Client closed connection')
                break    
        else:
            if data == "":
                line = " "
                try:
                    csockid.send(line.encode('utf-8'))
                except socket.error as err:
                    print('[S]: Client closed connection')
                    break
            else:
                line = data + " - TIMED OUT"
                try:
                    csockid.send(line.encode('utf-8'))
                except socket.error as err:
                    print('[S]: Client closed connection')
                    break

    ts1Socket.close()
    ts2Socket.close()
    ss.close()
    exit()
                
if __name__ == "__main__":
    ls(int(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), str(sys.argv[4]), int(sys.argv[5]))