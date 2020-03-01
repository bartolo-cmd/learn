#68. Coding a chat program
from datetime import datetime
import socket
import subprocess
import os
HOST = "192.168.1.4"
PORT = 6789
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print('Starting the Server At: ' , datetime.now())
print("Waiting for the incoming connection from client ...")

#nasłuchujemy do 5 prób połączenia
sock.listen(5)

client, addr = sock.accept()
#Musimy sprawdzić czy wartość "q" jest nie tylko wartością podaną przez klienta, ale także czy czasem serwer nie podał takiej wartości. Jeśli serwer poda taką wartość, a nie sprawdzimy tego, wyrzuci nam błąd, ponieważ program nie wie dlaczego zamknięto połączenie.
while True:
  data = client.recv(max_size)
  if data.decode('utf-8') == 'q':
    break
  
  #możemy także przechodzić do innego katalogu :)
  if data.decode('utf-8')[:2] =='cd':
    os.chdir(data.decode('utf-8')[3:])
  
  # wykonywać także takie rzeczy jak odpalenie różnych programów np. notatnika
  if data.decode('utf-8')[:2] =='start':
    subprocess.Popen('notepad',shell = True)
  
  
  print("At ", datetime.now(), addr, "said", data.decode('utf-8'))

  message_to_client = input("Enter message to client: ")
  message_to_client_encoded = message_to_client.encode('utf-8')
  client.send(message_to_client_encoded)
  if message_to_client == 'q':
    break

client.close()
sock.close()