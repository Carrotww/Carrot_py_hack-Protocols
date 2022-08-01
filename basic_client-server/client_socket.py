import socket

# s = socket.socket()
# 위 방식과 아래 방식이 있음
# 위 방식은 close()를 해주어야 함

with socket.socket() as s: # socket 불러오기
    addr = ("www.naver.com", 80) # second is port number
    s.connect(addr)
    s.send("GET /\n".encode()) # send data : web request
    data = s.recv(1024) # 1024 data 받기
    print(data.decode())