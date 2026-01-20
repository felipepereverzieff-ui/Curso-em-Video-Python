"""Aqui farei um programa que vai ler o ano de nascimento de um jovem e informar, de acordo com a idade desse jovem,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento.
Também mostrarei o tempo que falta ou que passou do prazo."""

from time import sleep
from datetime import date
from colorama import Back, Fore, Style, init
import sys # Usado para fechar o programa de vez no "sair"

init(autoreset=True) # Usado para auto-reset das cores no final do código

# Cores
blue = f"{Back.LIGHTWHITE_EX}{Fore.BLUE}{Style.BRIGHT}"
yellow = f"{Back.LIGHTWHITE_EX}{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Back.LIGHTWHITE_EX}{Fore.RED}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}"
green = f"{Back.LIGHTWHITE_EX}{Fore.GREEN}{Style.BRIGHT}"

def linha():
    # Função para evitar repetir o print do traço várias vezes.
    print("-=-" * 50)

while True:
    try:
        data_atual = date.today().year
        linha()
        ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))

        # Validação de entrada (filtro principal)
        if ano_de_nascimento > data_atual or ano_de_nascimento < 1900:
            print(f"{red}ERRO! DIGITE UM ANO ENTRE 1900 E {data_atual}.")
            continue # Volta ao início do loop até a entrada der certo

        # Cálculo e exibição
        idade_da_pessoa = data_atual - ano_de_nascimento
        linha()
        print(f"Em {data_atual}, você já tem ou terá {idade_da_pessoa} ano(s) de idade.")
        if idade_da_pessoa == 18:
            print(f"\n{green}Você deve se alistar esse ano.")
            linha()
        elif idade_da_pessoa < 18:
            linha()
            print(f"{red}Você ainda não está na idade de se alistar.")
            print(f"\n{white}Seu alistamento será daqui a {18 - idade_da_pessoa} ano(s), em {ano_de_nascimento + 18}.")
            linha()
        else:
            linha()
            print(f"{white}Você passou da idade de se alistar. Você deveria ter se alistado há {idade_da_pessoa - 18} anos.")
            linha()
    except ValueError:
        linha()
        print(f"{red}ERRO! Digite apenas números inteiros.")
        linha()
        continue # Ele só sai daqui enquanto validar tudo acima, senão ele repete antes de ir pro "sair"
    while True:
        sair = str(input("Deseja sair? [S/N] ")).strip().lower()
        if sair == "s":
            print("Saindo...")
            for c in range(3, -1, -1):
                sleep(0.3)
                print(c)
            print(f"{white}PROGRAMA FINALIZADO")
            sys.exit() # Fecha o programa de vez
        elif sair == "n":
            break # Volta ao loop principal, lá em cima
        else:
            print(f"{red}ERRO! DIGITE S OU N")
