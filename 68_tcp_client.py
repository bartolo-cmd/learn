import socket
from datetime import datetime

HOST = "192.168.1.4"
PORT = 6789
max_size = 1024

print("Starting The Client At: ", datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
#Musimy sprawdzić czy wartość "q" jest nie tylko wartością podaną przez klienta, ale także czy czasem serwer nie podał takiej wartości. Jeśli serwer poda taką wartość, a nie sprawdzimy tego, wyrzuci nam błąd, ponieważ program nie wie dlaczego zamknięto połączenie.

while True:
  message_to_server = input("enter message to server: ")
  message_to_server_encoded = message_to_server.encode('utf-8')
  if message_to_server == 'q':
    break
  data = s.recv(max_size)
  if data.decode('utf-8') == 'q':
    break
  print("At ", datetime.now(), "server replied with", data.decode('utf-8'))

s.close()
