import socket
import sys

if __name__=='__main__':
    serverip= '192.168.0.3'  # wifi ip을 알아오고 나서
    port = 9002
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((serverip,0))
    try:
        sock.connect((serverip,port))
        msg ='hello'
        sbuff=bytes(msg,encoding='utf-8')
        sock.send(sbuff)
        print("송신:{0}".format(msg))

        rbuff=sock.recv(1024)
        received=str(rbuff,encoding='utf-8')
        print('수신:{0}'.format(received))
    finally:
        sock.close()
