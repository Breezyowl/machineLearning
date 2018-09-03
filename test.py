from asynchat import async_chat
from asyncore import dispatcher
import asyncore
import socket

port= 5017
class ChatSession(async_chat):
    def __init__(self,sock):
        async_chat.__init__(self,sock)
        self.async_chat.set_terminator("\r\n")
        self.data=[]


    def collet_incoming_data(self,data):
        self.data.append(data)

    def found_terminator(self):
        line=''.join(self.data)
        self.data=[]
        print(line)


class ChatServer(dispatcher):
    def __init__(self,port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('127.0.0.1',port))
        self.listen(5)
        self.session=[]


    def handle_accept(self):
        conn,addr=self.accept()
        self.session.append(ChatSession(coon))
        print('connect from :',addr[0])

if __name__=='__main__':
    s = ChatServer(port)


    try:
        asyncore.loop()

    except KeyboardInterrupt:pass