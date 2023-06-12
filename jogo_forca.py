import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar_forca():
    limpar_tela()
    print("Bem-vindo ao Jogo da Forca!")
    palavra_secreta = input("Digite a palavra secreta: ").lower()
    limpar_tela()
    tentativas_permitidas = int(input("Digite a quantidade de tentativas que o jogador terá: "))
    limpar_tela()

    letras_acertadas = []
    letras_erradas = []
    tentativas_restantes = tentativas_permitidas

    while True:
        if len(letras_erradas) == tentativas_permitidas:
            limpar_tela()
            print("Suas tentativas acabaram! A palavra secreta era:", palavra_secreta)
            print("Fim de Jogo. Você perdeu!")
            break

        palavra_mostrada = ""
        for letra in palavra_secreta:
            if letra in letras_acertadas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "_ "

        if palavra_mostrada.replace(" ", "") == palavra_secreta:
            limpar_tela()
            print("Parabéns, você acertou todas as letras! A palavra secreta era:", palavra_secreta)
            print("Fim de Jogo. Você venceu!")
            break

        limpar_tela()
        print(f"Palavra secreta: {palavra_mostrada}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {' '.join(letras_erradas)}")

        escolha = input("Escolha uma opção:\n"
                        "1. Chutar um caractere\n"
                        "2. Chutar a palavra\n"
                        "3. Encerrar o programa\n"
                        "Escolha: ")

        limpar_tela()
        if escolha == "1":
            letra = input("Digite uma letra: ").lower()
            if letra in letras_acertadas or letra in letras_erradas:
                print("Essa letra já foi escolhida antes!")
            elif letra in palavra_secreta:
                letras_acertadas.append(letra)
                print("Você acertou uma letra!")
            else:
                letras_erradas.append(letra)
                tentativas_restantes -= 1
                print("Você errou uma letra!")
        elif escolha == "2":
            palavra = input("Digite a palavra: ").lower()
            if palavra == palavra_secreta:
                limpar_tela()
                print("Parabéns, você acertou a palavra! A palavra secreta era:", palavra_secreta)
                print("Fim de Jogo. Você venceu!")
                break
            else:
                letras_erradas.extend(palavra)
                tentativas_restantes -= 1
                print("Você errou a palavra!")
        elif escolha == "3":
            print("Você decidiu encerrar o programa.")
            break
        else:
            print("Opção inválida! Escolha novamente.")

        input("Pressione Enter para continuar...")

jogar_forca()