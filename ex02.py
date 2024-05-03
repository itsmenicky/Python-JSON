# Considere que o arquivo “users.json” apresenta o cadastro de usuários de um sistema.

# Faça um programa que a partir desse arquivo, gere uma lista de objetos de acordo com a classe especificada a 
# seguir:

#Classe Usuario
#   +identificador
#   +nome
#   +login
#   +email
#   +telefone


import json

class Usuario:
    def __init__(self, identificador, nome, login, email, telefone):
        self.identificador = identificador
        self.nome = nome
        self.login = login
        self.email = email
        self.telefone = telefone

lista_objetos = []
with open('users.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    for user in dados:
        objeto = Usuario(user["id"], user["name"], user["username"], user["email"], user["phone"])
        lista_objetos.append(objeto)

for item in lista_objetos:
    print(f"{item.identificador}\n{item.nome}\n{item.login}\n{item.email}\n{item.telefone}\n" + ("-"*30))