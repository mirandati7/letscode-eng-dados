def calcular_media(*args):
    print(args, type(args))
    
calcular_media(10,8,9)    

def calcular_media(*args):
    soma = sum(args)
    media = soma / len(args)    
    return media

print(calcular_media(10,8,9))        


def calcular_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)    
    return media + margem

print(calcular_media(10,8,9, margem = 0.3))    

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome = 'Pietro', sobrenome = 'Ribeiro')