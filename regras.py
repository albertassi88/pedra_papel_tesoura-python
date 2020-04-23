def reg(palavra_jogador, palavra_computador, nome):
    if (((palavra_jogador == 'papel') & (palavra_computador == 'pedra')) | ((palavra_jogador == 'tesoura') & (palavra_computador == 'papel')) | ((palavra_jogador == 'pedra') & (palavra_computador == 'tesoura'))):
       print(f'Parabéns {nome} você ganhou! você escolheu {palavra_jogador} e o computador escolheu {palavra_computador}.')
    elif (palavra_jogador == palavra_computador):
       print(f'Empatou! você escolheu {palavra_jogador} e o computador escolheu {palavra_computador}.')
    else:
       print(f'O computador ganhou! o computador escolheu {palavra_computador} e você escolheu {palavra_jogador}.')





