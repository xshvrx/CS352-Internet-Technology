import socket
import sys

def client(lsHostname, lsListenPort):
	try:
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client Socket Created")
	except socket.error as err:
		print('socket open error: {} \n'.format(err))
		exit()

	server_binding = (lsHostname, lsListenPort)
	print("[C]: Client will connect to LS at {}".format(server_binding))
	cs.connect(server_binding)
	print("[C]: Client connected to LS at {}".format(server_binding))
	
	inFile = open('PROJ2-HNS.txt', 'r')
	outFile = open('RESOLVED.txt', 'w')
    
	for line in inFile:
		cs.send(str(line).decode('utf-8'))
		newData = cs.recv(200).decode('utf-8')
		print(newData)
		outFile.write(newData + '\n')

	cs.close()
	outFile.close()
	inFile.close()
	exit()

if __name__ == "__main__":
    client(str(sys.argv[1]), int(sys.argv[2]))
print("Done.")