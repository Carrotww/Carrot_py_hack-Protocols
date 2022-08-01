import socket

with socket.socket() as s:
    addr = ("0.0.0.0", 80) # all addr allow
    s.bind(addr)
    s.listen() # server listen 상태로 전환
    print("start server..")

    conn, addr = s.accept() # connect accept
    print("accept {}:{}".format(addr[0], addr[1]))
    data = conn.recv(1024) # 원래는 데이터를 검증을 하고 보냄
    conn.send("200 Hi This is Web".encode())