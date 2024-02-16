# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos 
# e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


total_eleitores = int(input('Insira o numero total de eleitores do municipio: ->'))
total_brancos = int(input('Insira o numero total de votos em branco do municipio: ->'))
total_nulos = int(input('Insira o numero total de votos nulos do municipio: ->'))
total_validos = int(input('Insira o numero total votos validos do municipio: ->'))


porcentagem_brancos = (total_brancos *100) / total_eleitores
porcentagem_nulos = (total_nulos *100) / total_eleitores
porcentagem_validos = (total_validos *100) / total_eleitores


print(f'A porcentagem de votos em branco foi de {round(porcentagem_brancos, 2)}%')
print(f'A porcentagem de votos nulos foi de {round(porcentagem_nulos,2)}%')
print(f'A porcentagem de votos vakidos foi de {round(porcentagem_validos,2)}%')