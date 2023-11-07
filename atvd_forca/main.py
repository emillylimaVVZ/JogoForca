from biblioteca import JogoGeral

perg = 'sS'
while perg in 'sS':
    print("-------BEM VINDO AO JOGO DA FORCA!-------")

    opc = input("Pressione '1' para direcionar-se ao início do jogo.\n"
                 "Pressione '0' para sair do jogo: ")

    if opc == '0':
        print("Encerrando o Jogo.\n"
              "Obrigado por jogar.")
        break

    if opc == '1':
        JogoGeral()

    perg = input("Você deseja jogar novamente? (s/S para sim, qualquer outra tecla para não): ")

