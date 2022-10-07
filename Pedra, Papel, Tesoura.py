import random

computador = ['Pedra', 'Papel', 'Tesoura']
escolhapc = random.choice(computador)

print('1 = Pedra')
print('2 = Papel')
print('3 = Tesoura')
escolhauser = input(str('Digite sua escolha: '))
print('O PC escolheu:', escolhapc)

if escolhapc == 'Pedra' and escolhauser == '1':
    print('Você empatou!')
elif escolhapc == 'Pedra' and escolhauser == '2':
    print('Você ganhou!')
elif escolhapc == 'Pedra' and escolhauser == '3':
    print('Você perdeu!')
elif escolhapc == 'Papel' and escolhauser == '1':
    print('Você perdeu!')
elif escolhapc == 'Papel' and escolhauser == '2':
    print('Você empatou!')
elif escolhapc == 'Papel' and escolhauser == '3':
    print('Você perdeu!')
elif escolhapc == 'Tesoura' and escolhauser == '1':
    print('Você ganhou!')
elif escolhapc == 'Tesoura' and escolhauser == '2':
    print('Você perdeu!')
elif escolhapc == 'Tesoura' and escolhauser == '3':
    print('Você empatou!')