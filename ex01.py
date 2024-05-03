# Considere que o arquivo “notas.txt” apresenta uma listagem com os dados dos alunos de uma turma.

# Cada linha do arquivo apresenta os dados de um aluno, no formato:
# RA,NOME,NOTA1,NOTA2,NOTA3,NOTA4

# Implemente um programa que leia este arquivo de texto e a partir dele, gere um novo arquivo JSON no formato:
# {
#     "2101254": {
#         "nome": "Benício Pires",
#         "notas": [
#             3.6,
#             10.0,
#             8.5,
#             7.0
#         ]
#     },
#     "2101624": {
#         "nome": "Bruna Gonçalves",
#         "notas": [
#             9.5,
#             8.0,
#             6.0,
#             5.5
#         ]
#     }
# }


import json

alunos = []
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        dados = linha.split(',')
        aluno = {
            dados[0]: {
                "nome": dados[1],
                "notas": [float(dados[2]), float(dados[3]), float(dados[4]), float(dados[5])]
            }
        }
        alunos.append(aluno)

with open('notas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, ensure_ascii=False, indent=3)
