import json
from uuid import uuid1

class Estoque:
    def __init__(self, db_path: str):
        self.__start_database(db_path)


    def __start_database(self, db_path:str):
        try:
            with open(db_path, 'r'):
                print('Conectado ao banco de dados')
                self.db_path = db_path

        except FileNotFoundError:
            print('Arquivo do banco de dados não foi encontrado')


    def __get_dict(self):
            with open(self.db_path, 'r') as db:
                database_dict = json.load(db)
                return database_dict                


    def __save_dict_to_database(self, dict:dict):
        with open(self.db_path, 'w') as file:
            database = json.dumps(dict, indent=3)
            file.write(database)
        print("Alterações salvas no banco de dados")


    def get_product_by_id(self, code:str):
        database = self.__get_dict()
        item_exist = False
        for product in database:
            item = database.get(product)
            if item.get('code') == code:
                print(f'ID {item.get("code")} : Produto: {product} -> {item.get("qnt")} unidades no estoque')
                item_exist = True
        if item_exist == False:
            print("Produto não encontrado no banco de dados")


    def get_product_by_name(self, name:str):
        database = self.__get_dict()
        if name in database:
            item = database.get(name)
            print(f'ID {item.get("code")} : Produto: {name} -> {item.get("qnt")} unidades no estoque')
        else:
            print("Produto não encontrado no banco de dados")


    def show_all_products(self):
        database = self.__get_dict()
        print("=-"*30)
        print('ID | Nome | Quantidade\n')
        for product in database:
            item = database.get(product)
            print(f'{item.get("code")} | {product} | {item.get("qnt")}')
        print("=-"*30)


    def add_product(self, product_name:str, qnt:str):
        database = self.__get_dict()
        if product_name in database:
            database[product_name]["qnt"] = database[product_name]["qnt"] + int(qnt)
            print(f'Quantidade do produto {product_name} atualizada')
        else:
            database[product_name] = {"qnt":int(qnt), "code": str(uuid1())[0:8]}
        self.__save_dict_to_database(database)


    def check_items_quantity(self):
        database = self.__get_dict()
        print("=-"*30)
        print("=-"*30)
        for product in database:
            item = database.get(product)

            if item.get('qnt') <= 3:
                print(f'ATENÇÃO: PRODUTO {product.upper()} COM ESTOQUE BAIXO! {item.get("qnt")} ITENS RESTANTES')
        print("=-"*30)
        print("=-"*30)


    def remove_product_by_id(self, code:str, qnt:str ):
        database = self.__get_dict()
        for product in database:
            item = database.get(product)
            if item.get('code') == code:
                database[product]["qnt"] = database[product]["qnt"] - int(qnt)
                if database[product]["qnt"] < 0:
                    print("Não há quantidade suficiente em estoque deste item")
                    return
                item_exist = True

        if item_exist == False:
            print("Produto não encontrado no banco de dados")

        self.__save_dict_to_database(database)


    def remove_product_by_name(self, product_name:str, qnt:str ):
        database = self.__get_dict()
        if product_name in database:
            database[product_name]["qnt"] = database[product_name]["qnt"] - int(qnt)
        else:
            print("Produto não encontrado no banco de dados")

        self.__save_dict_to_database(database)


    def delete_product_by_name(self, product_name:str):
        database = self.__get_dict()
        if product_name in database:
            while True:
                print(f'Deseja remover o produto {product_name} do banco de dados?')
                confirm = input("[1] Sim    [2]Não\n")
                if confirm == "1":
                    del database[product_name]
                    break
                elif confirm =="2":
                    break
                else:
                    print('Opção Inválida')
                    continue
        else:
            print("Produto não encontrado no banco de dados")

        self.__save_dict_to_database(database)


    def delete_product_by_id(self, code:str):
        database = self.__get_dict()
        item_exist = False
        for product in database:
            item = database.get(product)
            if item.get('code') == code:
                item_exist = True
                while True:
                    print(f'Deseja remover o produto {product} do banco de dados?')
                    confirm = input("[1] Sim    [2]Não\n")
                    if confirm == "1":
                        del database[product]
                        break
                    elif confirm =="2":
                        break
                    else:
                        print('Opção Inválida')
                        continue
            if item_exist == False:
                print("Produto não encontrado no banco de dados")

        self.__save_dict_to_database(database)