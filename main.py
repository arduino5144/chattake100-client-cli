import socket

def receive_and_print_all_data(connection):
    connection.setblocking(1)
    data = connection.recv(1024)
    connection.setblocking(0)
    while len(data) > 1:
        print(data.decode('utf-8'), end='')
        data = connection.recv(1024)
    print()
    connection.setblocking(1)

client_multi_socket = socket.socket()
host = '127.0.0.1'
port = 2004

username = input("What is your username?")
password = input("What's the secret password?")
print('Waiting for connection response')
try:
    client_multi_socket.connect((host, port))
except socket.error as e:
    print(str(e))

client_multi_socket.send(str.encode("HELO " + username + ' ' + password))
res = client_multi_socket.recv(1024)
print(res.decode('utf-8'))
while True:
    Input = input('Hey there: ')
    client_multi_socket.send(str.encode(Input))
    receive_and_print_all_data()
    # res = client_multi_socket.recv(1024)
    # print(res.decode('utf-8'))
    # res = client_multi_socket.recv(1024)
    # print(res.decode('utf-8'))

