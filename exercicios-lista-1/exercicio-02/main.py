# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos 
# impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos 
# de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao 
# consumidor.


custo_fabrica = input('Insira o custo de fabrica do carro: -> ')

custo_distribuidor = int(custo_fabrica) * 0.28

custo_imposto = int(custo_fabrica)* 0.45

custo_final = int(custo_fabrica) + custo_distribuidor + custo_imposto

print(f'O custo final do carro ao consumidor é de: R${custo_final}')