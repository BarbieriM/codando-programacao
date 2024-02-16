# Simule um radar de rodovia 
# Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
# -O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa 
# deve indicar que a velocidade não foi fornecida
# -Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o 
# usuário deve mudar de mão
# -Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor 
# dessa multa o excesso de velocidade * 7
# -Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a 
# mecânica acima com o numero sorteado
from random import randint

velocidade_registrada = input('Insira a velocidade do registrada: -> ')

if velocidade_registrada == "":
    print('A velocidade não foi fornecida')
    velocidade_registrada = randint(1,120)

print(f'VELOCIDADE REGISTRADA: {velocidade_registrada}')

if int(velocidade_registrada) < 30:
    print('Velocidade abaixo do permitido, favor mudar de mão')

elif int(velocidade_registrada)>90:
    print(f'Velocidade acima do permitido, multa aplicada no excesso de velocidade: R${(int(velocidade_registrada) - 90) * 7}')