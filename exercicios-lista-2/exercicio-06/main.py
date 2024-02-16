alphabet ='abcdefghijklmnopqrstuvwxyz'

def create_list(text):
    text_in_list = []
    for letter in text:
        text_in_list.append(alphabet.index(letter))
    return text_in_list

def criptografar_mensagem(key_word, message):
    formated_message = message.replace(" ", "").lower()
    formated_key_word = key_word.replace(" ", "").lower()
    while len(formated_message) - len(formated_key_word) != 0:
        diference = len(formated_message) - len(formated_key_word)
        formated_key_word = formated_key_word + formated_key_word[0:diference]
    message_in_numbers = create_list(formated_message)
    key_word_in_numbers = create_list(formated_key_word)
    index = 0
    translated_message_in_list = []
    while index < len(key_word_in_numbers):
        encripted_letter_in_number = message_in_numbers[index] + key_word_in_numbers[index]
        if encripted_letter_in_number >25:
            translated_message_in_list.append(alphabet[encripted_letter_in_number - 25])
        else:
            translated_message_in_list.append(alphabet[encripted_letter_in_number])
        index = index +1
    print (''.join(translated_message_in_list))
def descriptografar_mensagem(key_word, encrypted_message):
    formated_message = encrypted_message.replace(" ", "")
    formated_key_word = key_word.replace(" ", "")
    while len(formated_message) - len(formated_key_word) != 0:
        diference = len(formated_message) - len(formated_key_word)
        formated_key_word = formated_key_word + formated_key_word[0:diference]
    message_in_numbers = create_list(formated_message)
    key_word_in_numbers = create_list(formated_key_word)
    index = 0
    translated_message_in_list = []
    while index < len(key_word_in_numbers):
        decripted_letter_in_number = message_in_numbers[index] - key_word_in_numbers[index]
        if decripted_letter_in_number < 0:
            decripted_letter_in_number = decripted_letter_in_number + 25
            translated_message_in_list.append(decripted_letter_in_number)
        else:
            translated_message_in_list.append(decripted_letter_in_number)
        index = index + 1
    print(translated_message_in_list)
    decripted_message = []
    for item in translated_message_in_list:
        decripted_message.append(alphabet[item])
    print(''.join(decripted_message))
    
while True:
    print('escolha uma opção')
    choice = input('[1]Criptografar texto [2]Descriptografar texto -->')
    if choice != "1" and choice !="2": 
        print("Por favor escolha uma das opções")
        continue
    else:
        if choice == "1":
            message = input("Insira o texto a ser criptografado -->")
            key = input("Insira a palavra chave para gerar a criptografia -->")
            criptografar_mensagem(key, message)
            break
        else:
            message = input("Insira o texto criptografado -->")
            key = input("Insira a palavra chave para gerar a criptografia -->")
            descriptografar_mensagem(key, message)
            break