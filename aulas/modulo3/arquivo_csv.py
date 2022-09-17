import csv
from hashlib import new

with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor) # pula uma linha
    for linha in leitor:
        if float(linha[2]) > 1:            
            print(linha)

with open('brasil_covid.csv', 'r' ) as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)

with open('users.csv', 'w', encoding='utf-8', newline ='') as arquivo_users:
    escritor  = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Pietro', 'Ribeiro', 'pietro@email.com', 'Masculino'])