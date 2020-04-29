#!/usr/bin/env python
import socketserver

class myHandler(socketserver.StreamRequestHandler):
    timeout = 5
    def handle(self):
        print("====  handling ...  ====")
        print("client address"+self.client_address)
        recvdata = ""
        while True:
            tmp = self.request.recv(16384)
            recvdata = recvdata + tmp.strip()
            if (len(tmp) < 16384):
                break;
        self.request.send("Received: {0}".format(recvdata))

class myApp(socketserver.TCPServer):
    def __init__(self, ip,port):
        socketserver.TCPServer.__init__(self, (ip, port), myHandler)
        print("server address"+self.server_address)
        try:
            self.serve_forever()
            print("====  server forever ====")
        except KeyboardInterrupt:
            print("Got keyboard interrupt, shutting down")
            self.shutdown()

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 9999
    app = myApp(ip,port)