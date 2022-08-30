#TheNutell
import os

from os import close


#Menu Principal
def main_main_menu_():
    import os
    print("\n" * os.get_terminal_size().lines)
    print("!Bem vindo ao Codes-Alot!")
    print("-----Menu Principal-----")
    print("1 Calculadora simples")
    print("")
    print("9 Fechar")
    menu_main = int(input(""))

    if menu_main == 1:
        main_menu_calculadora()
    if menu_main == 9:
        print("CHURULE CHURULE")
        pass


#Calculadora
def main_menu_calculadora():
    import os
    print("\n" * os.get_terminal_size().lines)
    print("---Menu Calculadora---")
    print("Selecione sua operação")
    print("1 Adição")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("")
    print("Caso deseje voltar ao menu principal aperte 9...")
    menu_calculadora = int(input(""))

    if menu_calculadora == 1:
        soma_()
    if menu_calculadora == 2:
        subtracao_()
    if menu_calculadora == 3:
        multiplicacao_()
    if menu_calculadora == 4:
        divisao_()
    if menu_calculadora == 9:
        main_main_menu_()

def soma_():
    print("")
    print("")
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 + numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu...")
    import os
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
    input("Aperte enter para voltar ao menu...")
    import os
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
    input("Aperte enter para voltar ao menu...")
    import os
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
    input("Aperte enter para voltar ao menu...")
    import os
    print("\n" * os.get_terminal_size().lines)
    main_menu_calculadora()

if __name__ == '__main__':
    main_main_menu_()