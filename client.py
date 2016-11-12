#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import socket
#req = "Hello tcp!"
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(('127.0.0.1', 1234))
#s.send(req)
#rsp = s.recv(1024)
#s.close()



import socket

sock = socket.socket()
sock.connect(('localhost', 1234))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()
print data