from set_task import set_task
from tasks import add_product, get_all_products, get_product_by_id, delete_product, get_product_by_name, display_low_qnt_products, remove_item_qnt

while True:
    task = set_task()

    if task == '1':
        print('-='*30)
        get_all_products()
        

    elif task == '2':
        print('Deseja buscar o produto pelo nome ou pelo ID?')
        while True:
            choice = input('[1] Nome    [2] ID   ')
            if choice != '1' and choice != '2':
                print('Por favor escolha uma opção válida')
            else:
                if choice == "2":
                    product_id = input(
                        'Insira o ID do produto que deseja buscar:    ')
                    print('-='*30)
                    get_product_by_id(product_id)
                    break
                else:
                    product_name = input(
                        'Insira o ID do produto que deseja buscar:  ')
                    print('-='*30)
                    get_product_by_name(product_name)
                    break

    elif task == '3':
        print('-='*30)
        product_name = input("Insira o nome do produto:    ")
        product_quantity = input("Insira a quantidade do produto:   ")
        add_product(product_name, product_quantity)

    elif task == '4':
        print('-='*30)
        product_id = input("Insira o ID do produto: ")
        delete_product(product_id)

    elif task == '5':
        product_id = input("Insira o ID do produto: ")
        product_quantity = input("Insira a quantidade do produto:   ")
        remove_item_qnt(product_id, product_quantity)

    elif task == '6':
        break
        

    display_low_qnt_products()
