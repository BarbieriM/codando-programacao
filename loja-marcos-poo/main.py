from menu import Menu
from estoque import Estoque

estoque_atual = Estoque("./database.json")

estoque_atual.check_items_quantity()
while True:
    menu = Menu.main_menu()
    if menu == "6":
        break
    else:
        Menu.execute_task(menu, estoque_atual)
        continue