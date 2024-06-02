import random

def escolher_palavra():
    palavras = ['python', 'jogo da forca', 'estacio', 'alan ', 'projeto']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao jogo da forca da estacio!")

    while tentativas_restantes > 0:
        print("\nPalavra: ", exibir_palavra(palavra, letras_corretas))
        print("Letras erradas: ", ' '.join(letras_erradas))
        print("Tentativas restantes: ", tentativas_restantes)
        
        tentativa = input("Adivinhe uma letra: ").lower()

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
        elif tentativa in palavra:
            letras_corretas.add(tentativa)
            print("Correto!")
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
            print("Errado!")

        if set(palavra) == letras_corretas:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

jogo_da_forca()
