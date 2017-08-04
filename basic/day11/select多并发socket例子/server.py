#Author:Cairo Li

import select,socket,sys,queue

server=socket.socket()
server.setblocking(0)

server_addr=('localhost',10000)

print('starting up on %s port %s'%server_addr)
server.bind(server_addr)

server.listen(5)

inputs=[server,]#自己也要检测自己，因为server本身是个fd(文件描述符)
outputs=[]
message_queues={}

while True:
    print("waiting for next event...")
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)#如果没有任何fd就绪，那程序就会一直阻塞在这里

    for s in readable:
        # 别忘记,上面我们server自己也当做一个fd放在了inputs列表里,传给了select,如果这个s是server,代表server这个fd就绪了,
        # 就是有活动了, 什么情况下它才有活动? 当然 是有新连接进来的时候 呀
        # 新连接进来了,接受这个连接
        if s is server:
            conn,client_addr=s.accept()
            print("new connnection from",client_addr)
            conn.setblocking(0)
            #为了不阻塞整个程序，我们不会立刻在这里开始接收客户端发来的数据，把它放到inputs里，
            #下一次loop时，这个新连接就会交给select去监听，如果这个连接的客户端发来了数据，那这个连接的
            #fd在server端就会变成就绪的，select就会把这个连接返回，返回到readable列表里，然后就可以loop
            #readable列表，取出这个连接，开始接收数据了，下面就是这么干的
            inputs.append(conn)

            message_queues[conn]=queue.Queue()#接收到客户端数据后，不会立刻返回，暂存在队列里，以后发送
        else:
            #s不是server的话，那就只能是一个与客户端建立连接的fd了
            data=s.recv(1024)
            if data:
                print("收到来自[%s]的数据:"%  s.getpeername()[0],data)
                message_queues[s].put(data)#先把数据放到queue里，一会返回给客户端
                if s not in outputs:
                    outputs.append(s)#为了不影响处理与其他客户端的连接，这里不立刻返回数据给客户端
            else:#如果收不到data代表客户端断开了
                print("客户端断开了",s)
                if s in outputs:
                    outputs.remove(s)#清理已断开的连接
                inputs.remove(s)#清理已断开的连接
                del message_queues[s]#清理已断开的连接

    for s in writeable:
        try:
            next_msg=message_queues[s].get_nowait()
        except queue.Empty:
            print("client[%s]"% s.getpeername()[0],"queue is empty")
            outputs.remove(s)
        else:
            print("send msg to [%s]"% s.getpeername()[0],next_msg)
            s.send(next_msg.upper())

    for s in exceptional:
        print("handling exception for",s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]




