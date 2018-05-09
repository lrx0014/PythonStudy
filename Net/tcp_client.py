import socket

HOST = '127.0.0.1'

PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except Exception as e:
    print('Connect Failed...')
    sys.exit()
while True:
    c = input("Type your msg:")
    s.sendall(c.encode())
    data = s.recv(1024)
    data = data.decode()
    print('Recieved:', data)
    if c.lower() == 'bye':
        break

s.close()