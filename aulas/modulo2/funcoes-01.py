def hello():
    print('Olá, mundo!')    

hello()

def calcular_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcular_media(10,10,10)
print(resultado)

resultado2 = calcular_media(valor1 = 10, valor2 = 9, valor3 = 9)
print(resultado2)

print('Ola, ', end =' ') 
print(', Pietro') 

def calcular_media2(valor1 = 0 , valor2 = 0, valor3 =0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcular_media2(10)
print(resultado)