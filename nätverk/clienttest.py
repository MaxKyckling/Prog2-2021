from socket import * 
def connect_to_server():
    s = socket()
    host = input("Ange serverns IP-adress: ")
    port = 12345
    s.connect((host, port))
    return s

s = connect_to_server()
b = s.recv(1024)
msg = b.decode("utf-16")
print(msg)
msg = input("Skriv något till servern: ")
b = msg.encode("utf-16")
s.send(b)
s.close()