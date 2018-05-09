import socket

words = {'how are you?':'Fine,thank you',
         'how old are you?':'22',
         'what is your name?':'Sam',
         'hello':'hi',
         'bye':'bye'}

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

print('Listening on port:', PORT)

conn, addr = s.accept()

print('Connected by:', addr)

while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('Recieved msg:', data)
    conn.sendall(words.get(data, 'Nothing').encode())

conn.close()

s.close()