empresa ='Google'
print(empresa)
empresa = "Let's Code"
print(empresa)

frase = "O professor Pietro da Let's Code disse: \"Hoje a pizza e por minha conta\""
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasilia"
nomes_cidades = nomes_cidades.split(',')
print(nomes_cidades)

# retirar espaço
cabecalho = "       MENU PRINCIPAL           "
print(cabecalho.strip())

nomes_cidade = 'rIo de jaNeirO'
print(nomes_cidade.title())
print(nomes_cidade.capitalize())
print(nomes_cidade.lower())
print(nomes_cidade.upper())

nome_cidade = input('Que cidade do Brasil e conhecida como cidade maravilhosa?')
nome_cidade = nome_cidade.strip()

while nome_cidade.lower() != 'rio de janeiro':
    print('Tenta de novo, vai')
    nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')

print('Booa, campeão!')    

#in
mensagem ='Você viu o que Pietro disse na sala ontem?'
fui_citado = 'Pietro' in mensagem
print(fui_citado) 