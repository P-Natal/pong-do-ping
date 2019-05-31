import os
import socket
import timeit
HOST_IP = "10.0.0.4"
PORT = 5001

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = (HOST_IP, PORT)

server = ('10.0.0.5', 5000)

print("Get ready for quiiiiite a lot of Pings!")

udp.bind(host)

msg = "Ping"

x = 1

results = open("results/pingTime-East-US.txt", 'w+')

while x <= 1000:
	ti = ((timeit.default_timer())*1000)
	udp.sendto(msg.encode(), server)
	print("Enviou!")
	data, cliente = udp.recvfrom(1024)
	print("Peguei!")
	tf = ((timeit.default_timer())*1000)

	if msg == "Ping":

		print("Servidor",str(cliente),"responde: ",data.decode())
		pingTime = tf-ti
		print("Tempo: ",pingTime,"ms")
		results.write(str(x) + " -> " + str(pingTime)+"\n")
		x = x + 1

results.close()
udp.close()
