import json
import os
prime_numbers = ['1', '2', '3', '5', '7']
def get_pi(n_decimals):
    path = os.path.join("exercicio-05", "pi.json")
    file = open(path)
    data = json.load(file)
    pi = str(data['pi'])
    sliced = (pi[2:n_decimals+2])
    return sliced
decimals = input('Insira o numero de casas decimais que você deseja analizar: ->')
greater_sequence = []
new_sequence = []
for number in get_pi(int(decimals)):
    if number in prime_numbers:
        new_sequence.append(number)
    else:
        if len(new_sequence) > len(greater_sequence):
            greater_sequence = new_sequence
            new_sequence = []
        else:
            new_sequence = []
if len(new_sequence) > len(greater_sequence):
    greater_sequence = new_sequence
print('a maior sequencia de numeros primos no intervalo indicado é: ', ''.join(greater_sequence))
