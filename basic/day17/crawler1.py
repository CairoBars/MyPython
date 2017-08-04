#Author:Cairo Li

import socket
"""
by default the sicket operations are blockingl:when the thread calls a methods
link connect or recv,it pauses until the operation completes
"""
def fetch(url):
    sock=socket.socket()
    sock.connect(('xkcd.com',80))
    request='GET {} HTTP/1.0\r\nHost:xkcd.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response=b''
    chunk=sock.recv(4096)
    while chunk:
        response+=chunk
        chunk=sock.recv(4096)

    #Page is now download
    links=parse_links(response)
    q.add(links)