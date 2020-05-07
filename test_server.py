import socket, errno


ip = '127.0.0.1'
port = 9999


'''
ip = '192.168.0.2'
port = 9002

ip = '127.0.0.1'
port = 9999


'''
line =[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("create server socket")

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((ip, port))
print("server socket bind. "+ip + ":"+str(port))

server_socket.listen()
print("server socket listen")

client_socket, addr = server_socket.accept()
print('Connected by', addr)


def parsing_data(self, data):
    tmp = ''.join(data)  # list로 들어 온 것을 스트링으로 합침
    print(tmp)
    return tmp


while True:
    try:
        data = client_socket.recv(1024)
        if data :
            line.append(chr(data))
            if data ==10:
                readystr = parsing_data(line)
                print('Received from', addr, readystr)

            if data.decode() == "finish":
                client_socket.close()
                print("clinet socket close")
                server_socket.close()
                print("server socket close")
                break

    except KeyboardInterrupt:
        break
        print("Got KeyboardInterrupt")
        client_socket.close()
        print("clinet socket close")
        server_socket.close()
        print("server socket close")


