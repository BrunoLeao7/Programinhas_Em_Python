import random

faces = int(input('Escreva o numero de faces do dado ou o numero 0 para sair: '))

if faces == 0:
    exit()
elif faces in[3, 4, 6, 8, 12, 20, 100]:
    numeros = list(range(1,faces+1))
    resultado = random.choice(numeros)
    print('O número que caiu foi: ',resultado)
else:
    print('Esse dado não existe!')