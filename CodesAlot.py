#TheNutell  2.2.0
import codecs
from operator import le
import os
import time
import random

from os import close

#Global porque sim
leaderboard_nomes = ["Joao", "Lucio", "Price", "Anna", "Lais"]
leaderboard_pontos = [[4, 7, 55], [12, 4, 88], [23, 45, 2], [12, 56, 6], [2, 1]]


#Menu Principal
def main_main_menu():
    menu_main = 0
    while menu_main != 9:
        print("\n" * os.get_terminal_size().lines)
        print("!Bem vindo ao Codes-Alot!")
        print("-----Menu Principal-----")
        print("1 Calculadora simples")
        print("3 jogo de Advinhação")
        print("")
        print("9 Fechar")
        menu_main = int(input("_"))

        if menu_main == 1:
            main_menu_calculadora()
            menu_main = 0
        if menu_main == 3:
            main_menu_advinha()
            menu_main = 0
        if menu_main == 9:
            print("CHURULE CHURULE")
            pass


#Calculadora
def main_menu_calculadora():
    print("\n" * os.get_terminal_size().lines)
    print("---Menu Calculadora---")
    print("Selecione sua operação")
    print("1 Adição")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("")
    print("9 Menu principal")
    menu_calculadora = int(input("_"))

    if menu_calculadora == 1:
        soma_()
    if menu_calculadora == 2:
        subtracao_()
    if menu_calculadora == 3:
        multiplicacao_()
    if menu_calculadora == 4:
        divisao_()
    if menu_calculadora == 9:
        pass

def soma_():
    print("")
    print("")
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 + numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu\n_")
    print("\n" * os.get_terminal_size().lines)
    main_menu_calculadora()

def subtracao_():
    print("")
    print("")
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 - numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu\n_")
    print("\n" * os.get_terminal_size().lines)
    main_menu_calculadora()

def multiplicacao_():
    print("")
    print("")
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 * numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu\n_")
    print("\n" * os.get_terminal_size().lines)
    main_menu_calculadora()

def divisao_():
    print("")
    print("")
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 / numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu\n_")
    print("\n" * os.get_terminal_size().lines)
    main_menu_calculadora()


#Adivinha
def main_menu_advinha():
    #Variaveis
    game = False
    numero_tentativa = 0
    numeros_advinha2 = 0
    min_chute = 0
    max_chute = 0
    #Variaveis

    print("\n" * os.get_terminal_size().lines)
    print("---Menu Jogo de Adivinha---")
    print("Ao iniciar o jogo sera escolhido um número aleatório e você tera que adivinhá-lo em um certo número de tentativas!")
    print("")
    print("Escolha a dificuldade") 
    print("1 Facil")
    print("2 Normal")
    print("3 Dificil")
    print("4 Impossivel")
    print("")
    print("8 LeaderBoard")
    print("9 Menu pricipal")
    menu_advinha = int(input("_"))

    
    if menu_advinha == 1:
        numeros_advinha2 = 50
        numeros_advinha = random.randrange(1, 50)
        game = True
    if menu_advinha == 2:
        numeros_advinha2 = 100
        numeros_advinha = random.randrange(1, 100)
        game = True
    if menu_advinha == 3:
        numeros_advinha2 = 150
        numeros_advinha = random.randrange(1, 150)
        game = True
    if menu_advinha == 4:
        numeros_advinha2 = 200
        numeros_advinha = random.randrange(1, 200)
        game = True
    if menu_advinha == 8:
        print("---Leaderboard---")
        for i in range(len(leaderboard_nomes)):
            print(f"{leaderboard_nomes[i]} : {leaderboard_pontos[i]}")
        print("\nAperte enter para voltar ao menu")
        input("_")
        main_menu_advinha()
    if menu_advinha == 9:
        pass

    while game == True:
        max_chute = numeros_advinha2
        print("Digite o seu nome para começar")
        nome_jogador = input("_")
        nome_jogador = nome_jogador.lower()
        nome_jogador = nome_jogador.capitalize()
        if nome_jogador not in leaderboard_nomes:
            leaderboard_nomes.append(nome_jogador)
            leaderboard_pontos.append([])     
            i = leaderboard_nomes.index(nome_jogador)
        if nome_jogador in leaderboard_nomes:
            i = leaderboard_nomes.index(nome_jogador)
        print(f"Um numero de 1 a {numeros_advinha2} foi escolhido \n   !!TENTE ENCONTRALO!!")
        game2 = True
        while game2 == True:
            tentativa = input("_")
            pergunta = tentativa.isdigit()
            if pergunta == True:
                tentativa = int(tentativa)
                numero_tentativa = numero_tentativa + 1
                if tentativa == numeros_advinha:
                    game = False
                    game2 = False
                    print(f"!!PARABENS {nome_jogador} VOCE ACERTOU EM {numero_tentativa}!!")
                    print("Deseja jogar novamente? \nSim 1 \nNão 2")
                    leaderboard_pontos[i].append(numero_tentativa)
                    fimdejogo = int(input("_"))
                    if fimdejogo == 1:
                        main_menu_advinha()
                    if fimdejogo >= 2:
                        print("O jogo fechara em 5 segundos")
                        time.sleep(5)
                        pass
                if tentativa > numeros_advinha:
                    if tentativa < max_chute:
                        max_chute = tentativa
                    print(f"Numero muito ALTO \nSeu numero esta entre {min_chute} e {max_chute}\n Tente novamente.")
                if tentativa < numeros_advinha:
                    if tentativa > min_chute:
                        min_chute = tentativa
                    print(f"Numero muito BAIXO \nSeu numero esta entre {min_chute} e {max_chute}\n Tente novamente.")
            if pergunta == False:
                print ("Sua tentativa tem que conter apenas numeros \nTente Novamente.")



if __name__ == '__main__':
    main_main_menu()
