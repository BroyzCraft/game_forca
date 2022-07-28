# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:04:25 2022

@author: x290372
"""


def menu():

    print("###  Jogo da Forca! ### \n")
    print("1 - Informar palavra e dica para o jogo.")
    print("2 - Jogar")
    option = int(input("Escolha uma opção: "))
    return option


def main():

    while True:

        option = menu()
        word = ''

        ### Valida se é possivel iniciar o jogo ou não. ###
        if (option == 2) and (word == ''):
            
            print('\n')
            print("--- ATENÇÃO ---")
            print("Antes de jogar, a palavra base e as dicas do jogo devem ser informadas. Tente novamente.")
            print('\n')
            
        else:
            
            ### Solicita todas as configurações do game ###
            if option == 1:
                
                word = input("\nInforme qual será a palavra utilizada no jogo: ")
                category = input("\nInforme qual a categoria de jogo: ")
                
                print("\nInforme 3 dicas com termos simples separados por virgulas.")
                print("Ex: Bola")
                print("Dicas : É redonda, usam em jogos de futebol, as pessoas chutam")
                tips = input("\nDicas: ")
                tips = tips.split(",")
                
                print('\n\nDEBUG')
                print(word.upper())
                print(category.upper())
                print(tips)

    pass


if __name__ == '__main__':
    main()
