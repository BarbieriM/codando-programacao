# Use a estrutura de loop for para que o programa retorne todos números pares de 0 até 
# um número especificado por terminal

numero_escolhido = int(input('Insira um numero ->'))

for x in range(numero_escolhido+1):
    if x % 2 == 0:
        print(x)