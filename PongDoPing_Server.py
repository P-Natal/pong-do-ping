import socket

HOST_IP = "10.0.0.5"
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST_IP, PORT)
udp.bind(orig)

while True:
	print("Esperando...")
	data, cliente = udp.recvfrom(1024)
	print("Servidor recebeu de", str(cliente),":",data.decode())
	udp.sendto(b"Pong", cliente)

udp.close()
