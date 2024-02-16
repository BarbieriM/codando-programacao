# Escreva um programa que leia os catetos oposto e adjacente de um triângulo e calcule a hipotenusa

cateto_oposto = float(input('Insira o valor do cateto oposto em cm: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente em cm: '))

hipotenusa = ((cateto_adjacente ** 2) + (cateto_oposto**2)) ** 0.5

print(f'o valor da hipotenusa do triangulo é {round(hipotenusa, 2)}')
