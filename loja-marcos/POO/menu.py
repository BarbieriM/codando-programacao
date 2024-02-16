from get_data import GetData
from estoque import Estoque

class Menu:
    def main_menu():
        return GetData.option_input("\n O que deseja fazer: \n [1] Ver todos os produtos   [2] Pesquisar produto\n [3] Adicionar produto       [4] Remover unidades de produto\n [5] Excluir produto         [6] Sair", ['1','2','3','4','5','6'])

    def execute_task(data:str, estoque:Estoque):
        if data == "1":
            estoque.show_all_products()
        elif data == "2":
            option = GetData.option_input("Deseja pesquisar pelo nome ou pelo codigo do produto? \n [1] Nome    [2] Codigo\n", ["1","2"])
            if option == "1":
                estoque.get_product_by_name(GetData.get_product_name())
            else:
                estoque.get_product_by_id(GetData.get_product_code())
        elif data == "3":
            estoque.add_product(GetData.get_product_name(), GetData.get_product_quantity(True))
        elif data == "4":
            option = GetData.option_input("Deseja remover o produto pelo nome ou pelo codigo? \n [1] Nome    [2] Codigo\n", ["1","2"])
            if option == "1":
                estoque.remove_product_by_name(GetData.get_product_name(), GetData.get_product_quantity(False))
            else:
                estoque.remove_product_by_id(GetData.get_product_code(), GetData.get_product_quantity(False))
        elif data == "5":
            option = GetData.option_input("Deseja deletar o produto do banco pelo nome ou pelo codigo? \n [1] Nome    [2] Codigo\n", ["1","2"])
            if option == "1":
                estoque.delete_product_by_name(GetData.get_product_name())
            else:
                estoque.delete_product_by_id(GetData.get_product_code())


    