import json
import uuid

path = 'database.txt'

def __open_database(db_path):
    database = open(db_path, 'r')
    database_products = database.read()
    products = database_products.split("\n")
    return products


def display_low_qnt_products():
    products = __open_database(path)
    for product in products:
        item = product.split('|')
        if int(item[2])<=3:
            print('-='*30)
            print(f'ATENÇÃO: PRODUTO {item[1].upper()} COM ESTOQUE BAIXO! {item[2]} ITENS RESTANTES')
            print('-='*30)
            


def get_all_products():
    products = __open_database(path)
    for product in products:
        item = product.split('|')
        print(f'ID {item[0]} : Produto: {item[1]} -> {item[2]} unidades no estoque')
    

def get_product_by_id(product_id):
    products = __open_database(path)
    item_exists = False
    for product in products:
        item = product.split('|')
        if item[0] == product_id:
            item_exists = True
            item_id = item[0]
            item_name = item[1]
            item_quantity = item[2]

    if item_exists:
        print(f'ID {item_id} : Produto: {item_name} -> {item_quantity} unidades no estoque')
    else:
        print('ID não encontrado')
    

def get_product_by_name(product_name):
    products = __open_database(path)
    item_exists = False
    for product in products:
        item = product.split('|')
        if item[1].lower() == product_name.lower():
            item_exists = True
            print(f'ID {item[0]} : Produto: {item[1]} -> {item[2]} unidades no estoque')

    if item_exists:
        pass
    else:
        print('Produto não encontrado')
    

def add_product(product_name, product_quantity):
    products = __open_database(path)
    update_database_products = []
    item_exists = False
    for product in products:
        item = product.split('|')
        if item[1].lower() == product_name.lower():
            item_exists = True
            item[2] = str(int(item[2]) + int(product_quantity))
            updated_product = f'{item[0]}|{item[1]}|{item[2]}'
            update_database_products.append(updated_product)
        else:
            update_database_products.append(product)
    if item_exists:
        new_database = open(path, 'w')
        new_database.write("\n".join(update_database_products))
        print(f'Quantidade do produto {product_name} atualizada')

    else:
        new_id = str(uuid.uuid1())[0:6]
        append_database = open(path, 'a')
        append_database.write(f'\n{new_id}|{product_name}|{product_quantity}')
        print(f'Produto {product_name} adicionado')
        
def delete_product(product_id):
    products = __open_database(path)
    updata_database_products = []
    item_exists = False
    for product in products:
        item = product.split("|")
        if item[0]==product_id:
            item_exists = True
            product_name = item[1]
            while True:
                print(f'Deseja remover o produto {product_name} do banco de dados?')
                confirm = input('[1] Deletar    [2]Não deletar')
                if confirm != '1' and confirm != "2":
                    print('opção inválida')
                else:
                    if confirm == '2':
                        return
                    else:
                        break
        else:
            updata_database_products.append(product)
    if item_exists:
        new_database = open(path, 'w')
        new_database.write('\n'.join(updata_database_products))
        print(f'O produto {product_name} ID:{product_id} foi removido do banco de dados')
    

def remove_item_qnt(product_id, product_quantity):
    products = __open_database(path)
    updatate_database_products = []
    item_exists = False
    for product in products:
        item = product.split("|")
        if item[0]==product_id:
            item_exists = True
            item[2] = str(int(item[2]) - int(product_quantity))
            updated_product = f'{item[0]}|{item[1]}|{item[2]}'
            updatate_database_products.append(updated_product)
        else:
            updatate_database_products.append(product)
    if item_exists:
        new_database = open(path, 'w')
        new_database.write('\n'.join(updatate_database_products))
    else:
        print('Item não encontrado na base de dados')    