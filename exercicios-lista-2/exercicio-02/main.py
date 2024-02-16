# Crie um sistema que:
# pergunte o nome do Aluno, 
# pergunte quantas matérias ele tem 
# qual é o nome de cada matéria
# qual foi sua nota em cada matéria
# No final o programa deve indicar se o aluno foi aprovado ou reprovado em cada uma das matérias, 
#   sendo a média 60%
# Retorne por qnts pontos o aluno foi reprovado ou quantos pontos extras ele teve acima da média


boletim= {}

print('Digite o nome do Aluno:')
nome_aluno = input('')

print('Insira o numero de materias que ele cursa:')
n_materias = int(input(""))
n=1
while n <= n_materias:
    print(f'Insira o nome da {n}ª  materia')
    nome_materia = input('')
    print(f'Insira a nota na materia {nome_materia} do aluno {nome_aluno} em 100')
    nota_materia = int(input(''))

    boletim[n] = {'nome_materia': nome_materia, 'nota_materia': nota_materia}
    n=n+1

for materia in boletim:
    nome = boletim[materia]['nome_materia']
    nota = boletim[materia]['nota_materia']
    if nota < 60:
        print(f'{nome} -> NOTA:{nota} REPROVADO POR {60-nota} PONTOS')
    else:
        print(f'{nome} -> NOTA:{nota} APROVADO POR {nota-60} PONTOS')
