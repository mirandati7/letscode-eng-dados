arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()

while linha != '':
    print (linha, end ='')
    linha = arquivo.readline()
arquivo.close()    


arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')

for linha in arquivo:
    print(linha, end='')
arquivo.close()    

# Print with
print("Print com with")
with open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto =  arquivo.read()
    print(texto)

# Escrita de arquivo
with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é uma linha que eu escrevi usando Python \n')
    arquivo.write('Essa é uma segunda linha que eu escrevi usando Python \n')

with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:    
    print(arquivo.read(), end='')

with open('arquivo_teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Essa é teceira linha que eu escrevi usando Python \n')

with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:    
    print(arquivo.read(), end='')    