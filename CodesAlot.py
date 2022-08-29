#TheNutell
import os

from os import close


global menu_


def main_menu():
    import os
    print("\n" * os.get_terminal_size().lines)
    print("-------Main Menu-------")
    print("Selecione sua operação")
    print("1 Adição")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("")
    menu_ = int(input("Caso deseje sair aperte 9:  "))
    if menu_ == 1:
        soma_()
    if menu_ == 2:
        subtracao_()
    if menu_ == 3:
        multiplicacao_()
    if menu_ == 4:
        divisao_()
    if menu_ == 9:
        print("CHURULE CHURULE")
        pass

def soma_():
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 + numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu...")
    import os
    print("\n" * os.get_terminal_size().lines)
    main_menu()

def subtracao_():
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 - numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu...")
    import os
    print("\n" * os.get_terminal_size().lines)
    main_menu()

def multiplicacao_():
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 * numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu...")
    import os
    print("\n" * os.get_terminal_size().lines)
    main_menu()

def divisao_():
    numero1 = int(input("Numero 1  "))
    numero2 = int(input("Numero 2  "))
    resultado_ = numero1 / numero2
    print("Seu resultado e: ", resultado_)
    print("")
    print("")
    input("Aperte enter para voltar ao menu...")
    import os
    print("\n" * os.get_terminal_size().lines)
    main_menu()

if __name__ == '__main__':
    main_menu()