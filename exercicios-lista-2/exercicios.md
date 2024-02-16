Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa, o programa pergunta se o usuário quer ou não continuar.
No final, quando a pessoa responder não, o programa deve indicar
Quantas pessoas são maiores de idade
Quantos homens
Quantas mulheres tem menos de 20 anos
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Crie um sistema que:
pergunte o nome do Aluno, 
pergunte quantas matérias ele tem 
qual é o nome de cada matéria
qual foi sua nota em cada matéria
No final o programa deve indicar se o aluno foi aprovado ou reprovado em cada uma das matérias, sendo a média 60%
Retorne por qnts pontos o aluno foi reprovado ou quantos pontos extras ele teve acima da média
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Criar um programa que peça valores numéricos em loop até que a pessoa negue colocar mais valores, depois o programa classifica os números:
do menor para maior número
do maior para o menor número
o menor número
o maior número
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(DESAFIO)
Crie um programa que transforme qualquer número romano em um número inteiro
Exemplo: XVIII sera transformado automaticamente no numero 18
O I corresponde ao número 1
O V corresponde ao numero ao 5
O X corresponde ao numero  10
O L corresponde ao numero 50
O C corresponde ao numero 100
O D corresponde ao numero 500
O M corresponde ao numero 1000
NUMERO DE LINHAS MAXIMAS: 50
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(DESAFIO)

Primos em Pi
Introdução:
Este desafio consiste em encontrar a sequência mais longa de números primos dentro das primeiras 10.000 casas decimais de π (o usuário do aplicativo poderá informar quantas casas decimais que ele quer que sejam analisadas) .
Em detalhes:
Localize a sequência mais longa de números primos (1, 2, 3, 5, 7) nas 
casas decimais de π sendo que o usuário informará quantos numerais deverão ser analizados
Em caso de mais de uma sequência do mesmo tamanho, a sequência com o 
início mais próximo do ponto inicial deverá ser utilizada.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

(DESAFIO)

Cifra de Vigenère

O Que é a cifra de Vigenère: 
http://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re

Desenvolva um algoritmo que consiga implementar a cifra de vigenere divididas entre duas funções

1- Codificar uma Mensagem: Uma função que receberá como entrada dois parâmetros, sendo eles uma palavra-chave (a chave que será usada para criptografar a mensagem) e uma mensagem que deverá ser criptografada. Quando executada, a função deverá aplicar o algoritmo de cifragem e retornar a frase cifrada.

2- Descodificar uma Mensagem: Uma função que receberá como entrada dois parâmetros, sendo eles uma palavra-chave (a chave que será usada para descriptografar a mensagem) e uma mensagem criptografada pela cifra de vigenère. Quando executada, a função deverá aplicar o algoritmo de descodificação da cifragem e retornar a frase descriptografada.

OBS: Caso a chave de criptografia for menor do que a mensagem que deverá ser criptografada, repita a chave de criptografia até satisfazer o tamanho da mensagem. 

Exemplo:
Chave de criptografia: “abc” -> 3 caracteres
Mensagem a ser criptografada: “patos são legais” -> 16 caracteres

Resultado: a chave deverá suprir os 16 caracteres ficando da seguinte forma: “abcabcabcabcabca”