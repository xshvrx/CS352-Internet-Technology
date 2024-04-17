import socket
import sys

def ts(tsListenPort):
	try:
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[S]: TS1 Socket Created")
	except socket.error as err:
		print('socket open error: {} \n'.format(err))
		exit()

	server_binding = ("", tsListenPort)
	ss.bind(server_binding)
	ss.listen(5)
	csockid, addr = ss.accept()
	
	host = socket.gethostname()
	print("[S]: Server host name is {}".format(host))
	localhost_ip = (socket.gethostbyname(host))
	print("[S]: Server IP address is {}".format(localhost_ip))
	
	while True:
		data = csockid.recv(200).decode('utf-8').strip().upper()
		inFile = open('PROJ2-DNSTS1.txt', 'r')
		
		for line in inFile:
			if data in line.upper():
				newData = line.strip() + ' IN'
				try:
					csockid.send(newData.encode('utf-8'))
				except socket.error as err:
					print('[S]: Client closed connection')
					exit()
				break

	csockid.close()
	ss.close()

if __name__ == "__main__":
    ts(int(sys.argv[1]))