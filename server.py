import socket
import json
import os

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

stop = 0

def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y

os.system('clear')
print("\n Servidor em funcionamento [✓]")

try:

  while (True):

    conn, addr = s.accept()
    print(" Conectado - Endereço de IP: [" + addr[0] + "] : Porta [" + str(addr[1]) + "]")
    print(" | IP: " + addr[0] + ":" + str(addr[1])) 
    data = conn.recv(1024) 
    json_data = json.loads(data)

    if json_data['choice']  == 1:
      print("\n\n | Resultado equivale a:")
      print(" → ", + json_data['num1'], "+", json_data['num2'], "=", add(json_data['num1'], json_data['num2']))
      break

    elif json_data['choice']  == 2:
      print("\n\n | Resultado equivale a:")
      print(" → ", + json_data['num1'], "-", json_data['num2'], "=", subtract(json_data['num1'], json_data['num2']))
      break

    elif json_data['choice']  == 3:
      print("\n\n | Resultado equivale a:")
      print(" → ", + json_data['num1'], "*", json_data['num2'], "=", multiply(json_data['num1'], json_data['num2']))
      break

    elif json_data['choice']  == 4:
      print("\n\n | Resultado equivale a:")
      print(" → ", + json_data['num1'], "/", json_data['num2'], "=", divide(json_data['num1'], json_data['num2']))
      break
    
  conn.close()

except KeyboardInterrupt:
  s.close()
