"""Aqui vou criar um programa que vai fazer o computador jogar Jokenpô com o user."""

from random import randint
from time import sleep
from colorama import init, Back, Fore, Style
init(autoreset=True)

def linha():
    print("-=-" * 20)

red = f"{Back.LIGHTWHITE_EX}{Fore.LIGHTRED_EX}{Style.BRIGHT}"
green = f"{Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}"

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')  # Criei lista para colocar as escolhas do input dentro
    computador = randint(0, 2)
    print("""Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
    while True:
        try:
            escolhadouser = int(input("Qual sua escolha? ")) - 1 # Usei -1 aqui para ter a possibilidade de usar 1,2,3 ao invés de
    # usar 0,1,2 que fica feio pra carambolas pro user digitar
            if 0 <= escolhadouser <= 2:
                break # Aqui só vai sair do loop se os números forem válidos
            print(f"{red}Erro! Escolha entre 1, 2 ou 3.")
        except ValueError:
            print(f"{red}Erro! Digite apenas números.")
    linha()
    print("PEDRA")
    sleep(0.5)
    print("PAPEL")
    sleep(0.5)
    print("OU TESOURA!!!")
    sleep(0.5)
    linha()
    print(f"Você escolheu: {itens[escolhadouser]}") # Se aqui não colocarmos escolha dentro de colchetes [], o print vai
    # mostrar o número ao invés do item
    linha()
    print(f"O computador escolheu: {itens[computador]}") # Igual ao de cima
    linha()
    if escolhadouser == 0: # PEDRA
        if computador == 0:
            print(f"{white}Empate!")
        elif computador == 1:
            print(f"{red}Você perdeu!")
        elif computador == 2:
            print(f"{green}Você ganhou!")
        linha()
    elif escolhadouser == 1: # PAPEL
        if computador == 0:
            print(f"{green}Você ganhou!")
        elif computador == 1:
            print(f"{white}Empate!")
        elif computador == 2:
            print(f"{red}Você perdeu!")
        linha()
    elif escolhadouser == 2: # TESOURA
        if computador == 0:
            print(f"{red}Você perdeu!")
        elif computador == 1:
            print(f"{green}Você ganhou!")
        elif computador == 2:
            print(f"{white}Empate!")
        linha()
    # Nesses if/elif, se não usarmos o 0,1,2 o programa vai travar ao digitar algum outro número, é só regra interna
    while True:
        sair = input(f"Deseja sair? [S/N] ").strip().lower()
        if sair == "s":
            print("Saindo do jogo...")
            for c in range(3, -1, -1):
                print(c)
                sleep(0.3)
            print("Fim do jogo!")
            exit()
        elif sair == "n":
            break
        else:
            print(f"{red}Erro! Digite S ou N.")
