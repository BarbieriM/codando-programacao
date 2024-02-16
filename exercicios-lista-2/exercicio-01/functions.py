def capture_data() ->dict:
    print('Insira a idade: -> ')
    age = input('')
    print('Insira o sexo(M, F, Outro): ->')
    sex = input('')
    data = {
            'age':int(age),
            'sex': (sex)
    }
    return data

def add_people(cout_people,json, data)-> dict:
    json[cout_people+1] = data
    return json

def get_age_18(json):
    count = 0
    for person in json:
        if json[person]['age'] >= 18:
            count = count + 1
    print(f'Foram registradas {count} maiores de idade nos dados.')

def get_woman_less_20(json):
    count = 0
    for person in json:
        if json[person]['sex'] == "F" and json[person]['age'] < 20:
            count = count + 1    
    print(f'Foram registradas {count} mulheres com menos de 20 anos nos dados')

def get_men(json):
    count = 0
    for person in json:
        if json[person]['sex'] == 'M':
            count = count + 1
    print(f'Foram registrados {count} homens nos dados') 
