import socket

addr = ("127.0.0.1", 4444)
str1 = input("echo: ").encode()
# client input -> echo 해줌

with socket.socket() as s:
    s.connect(addr)
    s.send(str1)
    data = s.recv(1024)

print(data.decode())