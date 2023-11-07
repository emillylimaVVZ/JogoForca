import random

def JogoGeral():
    def escolher_palavra():
        palavras = ["brasil", "bola", "computador"]
        return random.choice(palavras)
    chances = 4
    letras_usadas = []
    palavra_secreta = escolher_palavra()

    def dicas():
        if chances==1 and palavra_secreta=="brasil":
            print("Última chance! Dica: Maior país da América Latina.")
        if chances==1 and palavra_secreta=="computador":
            print("Última chance! Dica: Objeto principal para Programar.")
        if chances==1 and palavra_secreta=="bola":
            print("Última chance! Dica: Objeto para jogar Futebol.")

    while True:
        for letra in palavra_secreta:
            if letra in letras_usadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"Você tem {chances} tentativas.")

        tentativa = input("Digite uma letra para adivinhar: ").lower()
        letras_usadas.append(tentativa)

        ganhou = True
        for letra in palavra_secreta:
            if letra not in letras_usadas:
                ganhou = False

        if tentativa not in palavra_secreta:
            chances -= 1

        if chances ==1:
            print(dicas())

        if chances == 0 or ganhou:
            print(f"Suas tentativas acabaram! A palavra era: {palavra_secreta}")
            break

    if ganhou:
        print("Parabéns! Você venceu.")
    else:
        print(f"Você perdeu! A palavra era {palavra_secreta}")



