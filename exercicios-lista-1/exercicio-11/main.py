# Crie um script que receba 6 números e retorne quais são os números pares e quais 
# são os ímpares

number_1 = int(input('Insira o primeiro numero'))
number_2 = int(input('Insira o segundo numero'))
number_3 = int(input('Insira o teceiro numero'))
number_4 = int(input('Insira o quarto numero'))
number_5 = int(input('Insira o quinto numero'))
number_6 = int(input('Insira o sexto numero'))

numbers_list = [
    number_1,
    number_2,
    number_3,
    number_4,
    number_5,
    number_6
]
even_numbers = []
odd_numbers = []

for number in numbers_list:
    resto = number%2

    if resto == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print('Os numeros pares são:')
for number in even_numbers:
    print(number)

print('Os numeros impares são:')
for number in odd_numbers:
    print(number)