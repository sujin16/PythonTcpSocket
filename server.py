import socket, errno

ip = '127.0.0.1'
port = 9999


'''
ip = '192.168.0.3'
port = 9002

'''

# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("create server socket")

# 포트 사용중이라 연결할 수 없다는 WinError 10048 에러 해결를 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다. 
# PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.  
server_socket.bind((ip, port))
print("server socket bind. "+ip + ":"+str(port))

# 서버가 클라이언트의 접속을 허용하도록 합니다. 
server_socket.listen()
print("server socket listen")

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
client_socket, addr = server_socket.accept()
# 접속한 클라이언트의 주소입니다.
print('Connected by', addr)

while True:
    try:
        data = client_socket.recv(1024)
        #데이터가 들어올 때만  수신받은 문자열을 출력
        if data :
            '''
            # 빈 문자열을 수신하면 루프를 중지합니다.
            if not data:

                break
            '''
            print('Received from', addr, data.decode())

            # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
            # client_socket.sendall(data)

        if data.decode() =="finish":
            print("Got KeyboardInterrupt")
            client_socket.close()
            print("clinet socket close")
            server_socket.close()
            print("server socket close")

    except KeyboardInterrupt:
        break
        print("Got KeyboardInterrupt")
        client_socket.close()
        print("clinet socket close")
        server_socket.close()
        print("server socket close")


