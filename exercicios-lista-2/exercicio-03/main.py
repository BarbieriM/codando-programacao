number_list = []

while True:
    if len(number_list) == 0:
        value = input('Insira um valor numerico')
        try: 
            int(value)
            number_list.append(int(value))
            continue
        except:
            print('Valor fornecido não é um numero')
            continue
    else:
        while True:
            finalize = input("Deseja finalizar os registros de numeros: S ou N")
            if finalize != "S" and finalize !="N":
                print('Por favor digite "S" para sim e "N" para não')
                continue
            if finalize == "S":
                number_list.sort()
                print('sorted', number_list)
                number_list.reverse()
                print('reverse' ,number_list)
                greater_number = -9999999999
                for n in number_list:
                    if n > greater_number:
                        greater_number = n
                lesser_number = 9999999999
                for n in number_list:
                    if n<lesser_number:
                        lesser_number = n
                print('Greater' ,greater_number)
                print('lesser' ,lesser_number)
                break
            else:
                value = input('Insira um valor numerico ou outro tipo de valor para parar')
                try:
                    int(value)
                    number_list.append(int(value))
                    continue
                except:
                    print('Valor fornecido não é um numero')
                    continue
        
    break