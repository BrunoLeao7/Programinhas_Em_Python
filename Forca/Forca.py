from Art import stages
from Palavras import palavras, alfabeto
import random
import os

chutes = []
chances = 6
palavra_secreta = random.choice(palavras)
tamanho_palavra = str(len(palavra_secreta))

print('A palavra tem ' + tamanho_palavra + ' letras.')  

while True:

    print('Tentativas restantes: ', chances)

    for letra in palavra_secreta:
        if letra in chutes:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')

    print(stages[chances])

    chute = input('Digite a letra que desejas chutar ou SAIR para encerrar o programa: ').lower()
    os.system('cls')

    if chute == 'sair':
        break
    elif chute not in alfabeto or chute == '':
        print('Isso não é uma letra! Tenta de novo aí!')
        continue
    elif chute in chutes:
        print('Irmão, tu já tentou essa porra! Vai de novo ai cara...')
        continue
    chutes.append(chute)
    if chute in palavra_secreta:
        print('Tu é muito bom cara, acertou!')
    else:
        print('Muito ruim filho. Errou!')
        chances -= 1
    if chances == 0:
        print(stages[0])
        print('Vaza irmão, tu perdeu feio!')
        print('A palavra era',palavra_secreta, end ='.') 

        break
    elif set(palavra_secreta).issubset(set(chutes)):
        print('É... Tu ganhou, agora vaza!')
        break