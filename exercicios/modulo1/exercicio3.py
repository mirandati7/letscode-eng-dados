resposta_1 = input('1 - Mora perto da vítima     ..: S ou N ? ')
resposta_2 = input('2 - Já trabalhou com a vítima .: S ou N ? ')
resposta_3 = input('3 - Telefonou para a vítima  ..: S ou N ? ')
resposta_4 = input('4 - Esteve no local do crime ..: S ou N ? ')
resposta_5 = input('5 - Devia para a vítima      ..: S ou N ? ')

contador = int(0)

if resposta_1 == 'S' :    
    contador = contador + 1

if resposta_2 == 'S' :    
    contador = contador + 1

if resposta_3 == 'S' :    
    contador = contador + 1    

if resposta_4 == 'S' :    
    contador = contador + 1

if resposta_5 == 'S' :    
    contador = contador + 1    

print("Resultado da investigação: ", contador)
if contador <= 1:
    print("Liberados.")
elif contador == 2:
    print("Suspeitos.")    
elif contador >= 3 and contador <= 4:
    print("Cúmplices.")    
elif contador == 5:
    print("Assasinos.")    
