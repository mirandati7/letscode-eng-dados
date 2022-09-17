print("--------- FOR --------------")
nomes_cidades = ['São Paulo','Londres','Tóquio','Paris']
for nome in nomes_cidades:
    print(nome)

print("--------- WHILE --------------")
contador = 0
nomes_cidades = ['São Paulo','Londres','Tóquio','Paris']
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador = contador + 1

print("--------- FOR Tuplas --------------")
nomes_cidades = 'São Paulo','Londres','Tóquio','Paris'
for nome in nomes_cidades:
    print(nome)

print("--------- FOR Dicionario e dados --------------")
cidade = {
    'nome': 'São Paulo',
    'estado': 'SP',
    'populacao_milhoes': 12.2
}

for chave in cidade:
    print(f'{chave} : {cidade[chave]} ')

print("--------- FOR não altera--------------")
nomes_cidades = ['São Paulo','Londres','Tóquio','Paris']
for nome in nomes_cidades:
    nome ='Rio de Janeiro'

print("--------- FOR Range--------------")
nomes_cidades = ['São Paulo','Londres','Tóquio','Paris']
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de Janeiro'
print(nomes_cidades)    


print("--------- Range Imprime 10--------------")
print(list(range(10))) 
print("--------- Range Imprime de 2 a 10--------------")
print(list(range(2, 10))) 
print("--------- Range Imprime de 2 a 10 pulando de 2 em 2--------------")
print(list(range(2, 10, 2)))    
