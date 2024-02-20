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