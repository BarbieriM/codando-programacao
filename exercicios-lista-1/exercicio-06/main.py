# Crie um programa que peça ao usuário um número, e retorne todos os múltiplos do número escolhido pelo usuário 
# de 1 a 10


numero_escolhido = int(input('Insira um numero inteiro: '))

lista_de_multiplos = []

multiplo = 1

while multiplo <= 10:
    resto = numero_escolhido % multiplo

    if resto == 0:
        lista_de_multiplos.append(multiplo)
    multiplo = multiplo+1

n_multiplos = len(lista_de_multiplos)


print('Os multiplos entre 1 e 10 do numero escolhido são:')

primeiro = 1

while primeiro <= n_multiplos:
    print(lista_de_multiplos[primeiro-1])
    primeiro = primeiro+1