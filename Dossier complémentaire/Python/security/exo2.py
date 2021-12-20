import socket

host = "ftp.ibiblio.org"
port = 21
def fini():
    yolo = True

    while yolo:

        data = s.recv(2048)
        print (data.decode("utf-8"))
        if len(data) == 0:
            yolo = False
            pass
        else:
            break


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
fini()
s.send(b'USER anonymous\r\n')
fini()
s.send(b'PASS toto@tata.fr\r\n')
fini()
s.send(b'HELP\r\n')
fini()
s.send(b'QUIT\r\n')
s.close()


#cd Desktop\Cours\L3\Analyse Numérique\Extra\Programation\
