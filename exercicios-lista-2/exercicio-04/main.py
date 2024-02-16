roman_numbers = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
while True:
    get_roman_number = input('Digite o numero romano: ->')
    whole_number_list = []
    number_to_sum = []
    if "IIII" in get_roman_number or "XXXX" in get_roman_number or "MMMM" in get_roman_number or "VV" in get_roman_number or "LL" in get_roman_number or "DD" in get_roman_number:
        print('Numero inválido, por favor insira um numero romano valido')
        continue
    else:
        for letter in get_roman_number:
            whole_number_list.append(roman_numbers[letter])
    break
analyze_next_number = False
n_numbers = len(whole_number_list)
number_index = 0
while number_index < n_numbers:
    if number_index+1 == n_numbers:
        number_to_sum.append(whole_number_list[number_index])
        number_index = number_index+1
    else:
        number = whole_number_list[number_index]
        next_number = whole_number_list[number_index+1]
        if number < next_number:
            number_to_sum.append(next_number-number)
            number_index = number_index + 2
        else:
            number_to_sum.append(number)
            number_index = number_index + 1
print(sum(number_to_sum))