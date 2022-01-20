from socket import *

def start_server():
    s = socket()
    host = "localhost"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

s = start_server()
print("väntar på klient")
conn, addr = s.accept()
print("en klient anslöt sig från addressen", addr)
msg = "Servern säger hej till klienten! Hur mår du idag?"
b = msg.encode("utf-16")
conn.send(b)
print("väntar på meddelande från klienten")
b = conn.recv(1024)
msg = b.decode("utf-16")
print(msg)
conn.close()