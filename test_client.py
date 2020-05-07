import socket
import time

ip = '127.0.0.1'
port = 9999


'''
ip = '192.168.0.3'
port = 9002

'''


# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
client_socket.connect((ip, port))

for i in range(0,10):
    # 메시지를 전송합니다.
    time.sleep(1)
    client_socket.sendall('안녕'.encode())
    if(i ==9):
        time.sleep(1)
        client_socket.sendall('finish'.encode())

# 메시지를 수신합니다.
data = client_socket.recv(1024)
print('Received', repr(data.decode()))

# 소켓을 닫습니다.
client_socket.close()