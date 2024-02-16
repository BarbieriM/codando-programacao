# Use a estrutura de loop para que o programa retorne todos os múltiplos de 6 de 0 a 500.

primeiro = 1

print('Os multiplos de 6 entre 0 e 500 são:')

while primeiro <= 500:
    resto = primeiro % 6
    if resto == 0:
        print(primeiro)

    primeiro = primeiro + 1

