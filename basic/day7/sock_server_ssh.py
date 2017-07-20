#Author:Cairo Li

import os
import socket
server=socket.socket()
server.bind(('localhost'),9999)

server.listen()

while True:
    conn,addr=server.accept()
    print("new conn:",addr)
    while True:
        data=conn.recv(1024)
        if not data:
            print("客户端已断开")
            break

        print("执行命令：",data)
        cmd_res=os.popen(data.decode()).read()#执行结果也是字符串
        conn.send(cmd_res.encode("utf-8"))


server.close()