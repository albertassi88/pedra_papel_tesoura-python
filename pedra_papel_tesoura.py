import random
from jogo2 import regras

palavras = 'pedra', 'papel', 'tesoura'
palavra_computador = random.choice(palavras)

nome = input('Jogador - Qual é o seu nome?')
palavra_jogador = input(f'{nome} você escolhe "pedra", "papel" ou "tesoura"?')
palavra_nova_jogador = palavra_jogador
while ((palavra_nova_jogador != 'pedra') & (palavra_nova_jogador != 'papel') & (palavra_nova_jogador != 'tesoura')):
    palavra_correta = input('Favor digitar "PEDRA", "PAPEL" ou "TESOURA"')
    palavra_nova_jogador = palavra_correta

regras.reg(palavra_nova_jogador, palavra_computador, nome)











