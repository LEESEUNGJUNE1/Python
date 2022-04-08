# 단순 Echo server

from socket import *

serverSock = socket(AF_INET,SOCK_STREAM) # socket(소캣종류, 소캣유형)
serverSock.bind(('127.0.0.1',8888))
serverSock.listen(1)
print('server start . . .')

conn, addr = serverSock.accept()
print('client addr : ',addr)
print('from client message : ', conn.recv(1024).decode())
conn.close()
serverSock.close()