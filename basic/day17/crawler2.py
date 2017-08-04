#Author:Cairo Li
import  socket

sock=socket.socket()
sock.setblocking(False)
"""
A non-blocking socket throws an exception from connect ,even when
it is working normally.This exception replicates thr irritating 
behavior of the underlying C function,which sets errno to EINPROGRESS
to tell you it has begun
"""
try:
    socket.connect(('xkcd.com',80))
except BlockingIOError:
    pass