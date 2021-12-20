#Creation d'un serveur
import socket

host = ""
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

client, adresse=s.accept()
print(adresse)
print ("une connexion est etabli"),
print (client.getpeername())
client.close()
s.close()
