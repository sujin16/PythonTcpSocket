import socketserver
import sys

class TCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 :{0}'.format(self.client_address[0]))
        sock=self.request
        buf=sock.recv(1024)
        rec=str(buf,encoding='utf-8')
        print('수신:{0}'.format(rec))

        '''

        #client에게 data보내기

        sock.send(buf)
        print('송신:{0}'.format(rec))

        '''

        sock.close()
if __name__=='__main__':
    ip='192.168.0.3'
    port=9002
    server=socketserver.TCPServer((ip,port),TCPServer)
    print('start...')
    server.serve_forever()