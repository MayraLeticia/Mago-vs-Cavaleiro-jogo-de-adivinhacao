from random import randint

rodadas = 6
numero = ""

pontosMago = 0
vidaMago = 3
pontosCavaleiro = 0
vidaCavaleiro = 3

while rodadas != 0:

    numeroAleatorio = randint(1 ,10)
    if numeroAleatorio % 2 == 0: 
        numero = "par"
    else:
        numero = "impar"

    chuteMago = input("Faça a sua jogada: ")
    
    if numero == chuteMago:
        vidaCavaleiro = vidaCavaleiro - 1
        pontosMago = pontosMago + 1

        print("____________________________________\nO mago usou Bola de fogo.")
        print("O ataque do Mago foi super efetivo!")
        print("Você ganhou 1 ponto!\n__________________________________")

        rodadas = rodadas - 1
    else:
        vidaMago = vidaMago - 1
        pontosCavaleiro = pontosCavaleiro + 1
        print("____________________________________\nO Cavaleiro deferiu um ataque rapido.")
        print("O ataque do Cavaleiro foi super efetivo!")
        print("Você perdeu 1 ponto de vida!\n__________________________________")
        
        rodadas = rodadas - 1

    if vidaMago == 0:
        print("O mago desmaiou. A batalha terminou.")
        print("Você perdeu!\n__________________________________")

        rodadas = 0
    
    if vidaCavaleiro == 0:
        print("O Cavaleiro desmaiou. A batalha terminou.")
        print("Parabens, você ganhou! \n__________________________________")

        rodadas = 0

print("Pontos Cavaleiro: {}  Pontos Mago: {} \nVida do Cavaleiro: {} Vida do Mago: {}".format(pontosCavaleiro, pontosMago, vidaCavaleiro, vidaMago))



