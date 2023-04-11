#Tentar adivinhar o número que o computador escolheu aleatoriamente

import random

def palpite(x):
    numero_aleatorio = random.randint(1, x)
    palpite = 0
    while palpite != numero_aleatorio:
        palpite = int(input(f"Dê um palpite de um número entre 1 e {x}: "))
        if palpite < numero_aleatorio:
            print("Tente de novo. O número foi menor.")
        elif palpite > numero_aleatorio:
            print("Tente de novo. O número foi maior.")
        print(palpite)

    print(f"Parabéns! Você adivinhou o número certo! O número era {numero_aleatorio}")

#O computador vai tentar adivinhar o número que você escolheu
def palpite_computador(x):
    menor = 1
    maior = x
    feedback = ""

    while feedback != "c":
        if menor != maior:
            palpite = random.randint(menor, maior)
        else:
            palpite = menor
        feedback = input(f"O palpite {palpite} foi muito alto(A) ou muito baixo(B), ou o palpite estava certo(C)? ").lower()
        if feedback == "a":
            maior = palpite - 1
        elif feedback == "b":
            menor = palpite + 1

    print(f"Parabéns, o computador acertou o {palpite} corretamente!")

palpite_computador(10)