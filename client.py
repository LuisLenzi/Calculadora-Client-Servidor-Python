import socket 
import json
import os

HOST = 'localhost' 
PORT = 50000 

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

stop = 0

while (True):

  os.system('clear')
  print("\n | Calculadora")
  print(" | Equipe: Luís Lenzi, Guilherme Cruz, Hugo Massote e Victor Bento.")
  print("\n [1] - Adição")
  print(" [2] - Subtração")
  print(" [3] - Multiplicação")
  print(" [4] - Divisão")

  choice = int(input("\n → Digite um número de refêrencia para o operador desejado: [1][2][3][4]: "))
  num1 = float(input(" Digite o primeiro valor: "))
  num2 = float(input(" Digite o segundo valor: "))

  json_object = {"choice": choice, "num1": num1, "num2": num2}
  data = json.dumps(json_object)
  connection.send(data.encode()) 

  print ('\n [Valores enviados para o servidor]')

  connection.close()
  break
