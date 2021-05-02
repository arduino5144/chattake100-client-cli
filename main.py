import socket
from _thread import *


def receive_and_print_all_data(connection):
    while True:
        data = connection.recv(1024)
        print(data.decode('utf-8'), end='')


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

client_multi_socket.send(str.encode("/HELO " + username + ' ' + password))
start_new_thread(receive_and_print_all_data, (client_multi_socket, ))
# res = client_multi_socket.recv(1024)
# print(res.decode('utf-8'))
while True:
    Input = input()
    client_multi_socket.send(str.encode(Input))
    # receive_and_print_all_data(client_multi_socket)
    # res = client_multi_socket.recv(1024)
    # print(res.decode('utf-8'))
    # res = client_multi_socket.recv(1024)
    # print(res.decode('utf-8'))

