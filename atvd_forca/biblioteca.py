import random


def JogoGeral():

    ganhou= False
    palavra="brasil"

    chances=4
    letras_usuarios=[]

    while True:
        for letra in palavra:
            if letra.lower() in letras_usuarios:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"Você tem {chances} tentativas.")

        tentativa = input("Digite uma letra para advinhar: ")
        letras_usuarios.append(tentativa.lower())


        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_usuarios:
                ganhou=False

        if tentativa.lower() not in palavra.lower():
            chances-=1

        if chances==1:
            print("Última tentativa!Dica: Maior país da América Latina!")

        if chances==0 or ganhou:
            print(f"Suas tentativas acabaram! a palavra era: {palavra}")
            break


    if ganhou:
        print(f"Parabéns! Você venceu.")

    else:
        print(f"Você perdeu! A palavra era {palavra}")


