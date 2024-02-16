(DESAFIO)
Crie um jogo RPG por turnos de console

-O programa deve permitir o usuário à escolher entre dois personagens (mago ou guerreiro)
    
    Caso o usuário escolha guerreiro o programa deve sortear um valor aleatório entre 5 e 10 que será a barra de poder do guerreiro 

    Caso o usuário escolha mago o programa deve sortear um valor aleatório entre 7 e 15 que será a barra de poder do mago

-Dentro do jogo o usuário terá 4 opções:
    
    Atacar (sorteia um valor de 3 a 10 de dano caso o usuário tenha escolhido guerreiro ou sorteia um valor entre 0 e 8 caso o usuário tenha escolhido um mago, independente do personagem escolhido o jogador gasta 2 de poder por ataque)

    Defender (cancela 1 ataque do inimigo, caso o usuário seja um mago o jogador gasta 1 de poder de ataque), 

    Curar (cura 1 de vida no caso do guerreiro e 4 de vida no caso do mago)

    Descansar (sorteia um valor entre 1 e 5 e usa este valor para recuperar pontos de poder)

-Monstros

    Os monstros são gerados com 20 de vida

    Para atacar o monstro em seu turno escolhe aleatoriamente entre atacar dando 3 de dano ou se defender

    Quando algum monstro é morto, o usuário tem a opção de sair do jogo ou continuar

    Caso o usuário após matar um monstro queira continuar jogando, toda a sua vida é recuperada e o próximo monstro gerado terá 10 de vida e 3 de ataque a mais que o último e o jogador ganhará mais 3 de probabilidade de ataque e mais 5 de vida