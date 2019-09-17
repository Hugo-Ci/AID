import os
from socket import *
import signal

def handle(c):
    while True:
        date = c.recv(1024)
        if date == '':# if date =='' 和　if not date 的区别, os_exit(0)　和　sys.exit() 的区别
                        #setsockopt(self, level, option, value) value 的作用
            break
        print(date.decode())
        c.send(b'OK')
    c.close()


HOST = '0.0.0.0'
POST = 9999
ADDR = (HOST,POST)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print('Listen the port 8888...')
while True:
    try:
        c,addr = s.accept()
        print('Connect from',addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)

        os._exit(0)
    else:
        c.close()

