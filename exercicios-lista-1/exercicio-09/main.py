# Simule uma tentativa de criar uma conta em uma plataforma digital
# -O programa deve conferir se a conta do usuário que está sendo criado possui no 
# mínimo 12 caracteres e tenha uma senha que possua de no mínimo 8 caracteres e 
# caracteres numéricos 
# -O programa também deve barrar a entrada de caracteres especiais na criação do 
# nome de usuário
# -O programa só deve criar a conta caso todas as condições tenham sido concluídas, 
# se não o programa deve reiniciar voltando para o primeiro processo
# -Quando a conta for criada o programa deve printar a frase: "conta criada!"

from verifications import verify_special_characters, verify_number

print('Criação de novo usuário')

while True:
    user_name = input('Insira o novo nome de usuário: -> ')

    if verify_special_characters(user_name):
        print('Não é permitido o uso de caracteres especiais no nome de usuário')
        continue

    elif len(user_name)<12:
        print('O nome de usuário deve conter pelo menos 12 caracteres')
        continue

    else:
        print('Nome de usuário Válido')
        break

while True:
    password = input('Insira a nova senha: -> ')

    if len(password)<8:
        print('A senha deve conter pelo menos 8 caracteres')
        continue

    elif not verify_number(password):
        print('A senha deve conter pelo menos um caractere númerico')
        continue

    else:
        print('CONTA CRIADA COM SUCESSO!')
        break
