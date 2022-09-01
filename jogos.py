import adivinhacao
import forca

print("#############")
print("_Jogos em python_")
print("#############")

play = int (input("Escolha seu jogo. Digite 1 para Jogo da Adivinhação ou 2 para Jogo da Forca "))

if(play == 1):
    print("Jogo adivinhação")
    adivinhacao.jogar_advinhacao()

elif(play == 2):
    print(" Jogo da forca!")
    forca.jogar_forca()