import socket
import sys

host = sys.argv[1]
port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port=int(port)
except ValueError:
    port = socket.getservbyname(port,"udp")
s.connect((host,port))
print("Veuillez entrer les donnees a transmetre")
data = sys.stdin.readline().strip()
s.sendall(data.encode())
print ("attente de reponse, Ctrl-C pour arreter")

yolo = True

while yolo:
    data = s.recv(2048)
    print (data.decode())
    if not len(data):
        yolo = False
        break

#cd \Users\PC\Desktop\Cours\L3\Analyse Numérique\Extra\Programation
