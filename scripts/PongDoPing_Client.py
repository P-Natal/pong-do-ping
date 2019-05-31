import socket
import timeit

hostname = socket.gethostname()
HOST_IP = socket.gethostbyname(hostname)
PORT = 5001

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = (HOST_IP, PORT)
udp.bind(host)

serverIP = input("What's the destiny Server IP Address? ")
server = (str(serverIP), 5000)

serverRegion = input("What's the destiny Server region? (Ex. East-US): ")
serverRegion = serverRegion.replace(" ", "")

results = open("results/pingTime" + str(serverRegion) + ".txt", 'w+')

print("Get ready for quiiiiite a lot of Pings!")

msg = "Ping"

for x in range(1000):
    x += 1
    ti = ((timeit.default_timer()) * 1000)
    print(server)
    udp.sendto(msg.encode(), server)
    data, cliente = udp.recvfrom(1024)
    tf = ((timeit.default_timer()) * 1000)

    if msg == "Ping":
        print("Server", str(cliente), "responds: ", data.decode())
        pingTime = tf - ti
        print("Time: ", pingTime, "ms\n")
        results.write(str(x) + " -> " + str(pingTime) + "\n")

results.close()
udp.close()
