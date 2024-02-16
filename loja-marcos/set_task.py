def set_task():
    return input_choice("\n O que deseja fazer: \n [1] Ver todos os produtos        [2] Pesquisar produto\n [3] Adicionar produto            [4] Excluir produto\n [5] Remover unidades de produto  [6] Sair", ['1','2','3','4','5','6'])
    

def input_choice(message, choice):
    print(message)
    user_choice = input('')
    if user_choice in choice:
        return user_choice
    else:
        print('Por favor escolha uma opção válida')