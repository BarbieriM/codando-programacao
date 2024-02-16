from functions import capture_data, add_people, get_age_18, get_men, get_woman_less_20

n_people = 0
people_hashmap = {}

while True:
    if len(people_hashmap) == 0:
        data = capture_data()
        people_hashmap = add_people(n_people, people_hashmap, data)
        n_people = n_people + 1
        continue
    else:
        while True:
            print('Deseja registrar mais dados? Digite "S" ou "N" -> ')
            more_data = input('')
            if more_data != "S" and more_data != "N":
                print('Por favor digite "S" para sim e "N" para não')
                continue
            elif more_data == "S":
                data = capture_data()
                people_hashmap = add_people(n_people, people_hashmap, data)
                n_people = n_people + 1
            else:
                get_age_18(people_hashmap)
                get_woman_less_20(people_hashmap)
                get_men(people_hashmap)
                break
    break