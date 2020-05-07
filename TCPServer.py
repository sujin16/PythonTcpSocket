import socketserver
import sys


class TCPServer(socketserver.BaseRequestHandler):

    def space_count(self,string):
        count =0
        for a in string:
            if(a.isspace()) ==True:
                count +=1
        return str(count)

    def handle(self):
        print('client address  :{0}'.format(self.client_address[0]))
        while True:
            try:
                sock=self.request
                buf=sock.recv(1024).strip()
                result_str=str(buf,encoding='utf-8')

                #1. sensor data 를 받아옴
                if result_str !='':
                    print('Received:' +result_str)
                elif result_str =='':
                    print('Received:' + self.space_count(result_str))


            except Exception:
                print("exception")
                sock.close()
                print('socket server disconnect')
                break


        '''

         if result_str in 'Measure file':
                    print('Received:{0}'+result_str)

                elif result_str in 'Result value':
                    print('Received:{0}'+  result_str)

                elif result_str !='':
                    print('Received:'+ len(result_str))

                elif result_str =='\n':
                    print('Received:{0} sdf', result_str)


        #client에게 data보내기

        sock.send(buf)
        print('송신:{0}'.format(rec))

        sock.close()
        print('socket server disconnect')

        '''


if __name__=='__main__':
    '''
    ip = '192.168.0.2'
    port = 9002

    ip = '127.0.0.1'
    port = 9999

    '''

    ip = '192.168.0.4'
    port = 9002

    server=socketserver.TCPServer((ip,port),TCPServer)
    print('start...')
    server.serve_forever()