#Trilha Engenheiro de dados
#Alex Miranda de Oliveira
#Exercicio 2A
idade = int(input('Digite a sua idade:'))

if idade >= 0 and idade <= 150:
    print("Idade dentro do intervalo" ,idade)
else:
   print("idade inválida")

#Exercicio 2B
salario = float(input('Informe o salário:'))

if salario > 0:
    print("Valor do Salário :", salario)
else:
    print("Salário invalído")

#Exercicio 2C
sexo_informado = input('Informe o sexo M,F ou Outro:')
sexo = ['M','F','Outro']

if sexo.__contains__(sexo_informado):
    print("Sexo valido")
else:
    print("Sexo invalido")
