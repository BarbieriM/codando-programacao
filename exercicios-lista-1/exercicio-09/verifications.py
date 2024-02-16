def verify_special_characters(text:str)-> bool:
    special_characters = False
    special_character_list = [
        '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', 
        '{', '[', ']', '}', '|', '\\', ':', ';', '"', "'", '<', ', ', '>', '.', '?', 
        '/']
    

    for character in special_character_list:
        if character in text:
            special_characters = True
    
    return special_characters

def verify_number(text:str)-> bool:
    number_in_text = False
    numbers_list = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0'
    ]

    for number in numbers_list:
        if number in text:
            number_in_text = True
    
    return number_in_text