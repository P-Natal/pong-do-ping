import socket
HOST_IP = "127.0.0.1"     # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST_IP, PORT)
udp.bind(orig)

while True:
	data, cliente = udp.recvfrom(1024)
	print("Servidor recebeu de", str(cliente),":",data.decode())
	udp.sendto(b"Pong", cliente)

udp.close()