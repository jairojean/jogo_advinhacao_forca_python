import random

def jogar_advinhacao():
    print("#############")
    print("_Jogo_de_advinhação_")
    print("#############")

    secret_number = int( random.randrange (1 , 10))
    level = int(input("Escolha o nivel que você deseja 1 ,2 ou 3 :"))
    print("################# ")
    if(level == 1):
        attempts = 10
        print("Nivél 2 - Médio, você tem",attempts , " tentativas")
    elif(level == 2):
        attempts = 5
        print("Nivél 2 - Médio, você tem: ", attempts, " tentativas")
    elif(level == 3):
        attempts = 3
        print("Nivél 3 - Difícil você tem: ", attempts, " tentativas")


    for i in range (0,10):
        print("################# ")
        print("Tentativa numero ", i)

        n1 = input("Digite seu palpite entre 1 e 10:  ")
        number = int(n1)

        good = secret_number == number
        bigger = secret_number < number
        smaller = secret_number > number

        if(good):
            print("O numero secreto é:", secret_number)
            print("Parabéns, você acertou!!")
            break
        else:
            if(bigger):
                print("Você digitou um numero maior que o numero secreto.")
            elif(smaller):
                print("Você digitou um numero menor que o numero secreto.")
        i += 1
    print(" Final de Jogo! O numero secreto é:", secret_number)

if(__name__ == "__main__"):
    jogar_advinhacao()