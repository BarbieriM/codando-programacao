class GetData:
    def option_input(text:str, options:list[str]):
        while True:
            option = input(f'{text}\n')
            if option in options:
                return option
            else:
                print("Opção Inválida")
                continue

    def get_product_name():
        return input("Insira o nome do produto\n")

    def get_product_code():
        return input("Insira o codigo do produto\n")

    def get_product_quantity(add_or_remove:bool):
        if add_or_remove:
            return input("Insira a quantidade a ser adicionada\n")
        else:
            return input("Insira a quantidade a ser retirada\n")
    
