import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

username = input("What is your username?")
password = input("What's the secret password?")
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

ClientMultiSocket.send(str.encode("HELO " + username + ' ' + password))
res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'))
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))