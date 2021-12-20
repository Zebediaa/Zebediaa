import socket
import sys

host = sys.argv[1]
port = sys.argv[2]
fichier = sys.argv[3]

print ('Creation du socket ...')
try:

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error() as e:
    print ('Erreur lors de la création du socket : {}'.format(e))
    sys.exit(1)
try:
    print ('[+] Connexion  |Port: {} |Host: {}'.format(port, host) )
    s.connect(("www.eni.fr", 80))
except socket.gaierror() as e:
    print ("Erreur adresse : {}".format(e))
    sys.exit(1)
print ('Connexion etablie')
send = (('GET /{} HTTP/1.0\r\n\r\n').format(fichier))
send = send.encode()
try:
    s.send(send)
except socket.error() as e:
    print ("Erreur envoi : {}".format(e))
    sys.exit(1)
connect = True
while connect:
    try:
        data = s.recv(1024)

    except socket.error() as e:
        print ('Erreur de reception : {}'.format(e))
        sys.exit(1)
    print (data)
    if not len(data):
        connect = False
s.close()
