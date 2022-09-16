#Lista de dados
nomes_paises =['Brasil', 'Argentina','China', 'Canada','Japao']
print(nomes_paises)
#de 1 a 3 na lista
print(nomes_paises[1:3]) 
#ate o 2 item
print(nomes_paises[:2])
#pula de 2 em 2
print(nomes_paises[::2])
#o -1 inverte a lista
print(nomes_paises[::-1])

print("Brasil" in nomes_paises)
print("Canada" not in nomes_paises)


lista_capitais = []
lista_capitais.append('Brasilia')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')
print(lista_capitais)

lista_capitais.insert(2, 'Paris')
print(lista_capitais)

lista_capitais.remove('Buenos Aires')
print(lista_capitais)

removido = lista_capitais.pop(2)
print(lista_capitais, removido)

#Tupla de dados
nomes_paises = 'Brasil', 'Argentina','China', 'Canada','Japao'
len(nomes_paises)
print(nomes_paises[0])
b,a , c, ca ,j = nomes_paises
print(b, c, j)
print(*nomes_paises)





