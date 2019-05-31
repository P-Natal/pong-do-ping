import socket

hostname = socket.gethostname()
HOST_IP = socket.gethostbyname(hostname)
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = (HOST_IP, PORT)
udp.bind(server)

print("Running Server at: " + str(server))

while True:
	data, client = udp.recvfrom(1024)
	print("Servidor recebeu de", str(client), ":", data.decode())
	udp.sendto(b"Pong", client)

udp.close()