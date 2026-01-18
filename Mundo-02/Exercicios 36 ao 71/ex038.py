"""Aqui vou criar um programa que vai ler 2 números inteiros e comparar eles, mostrando na tela:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""

from colorama import Fore, Back, Style, init
from time import sleep

init(autoreset=True) # Aqui ele inicia o colorama e limpa as cores após cada print, automaticamente

# Cores pré-definidas para facilitar a manutenção delas dentro do programa
blue = f"{Back.LIGHTWHITE_EX}{Fore.BLUE}{Style.BRIGHT}"
yellow = f"{Back.LIGHTWHITE_EX}{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Back.LIGHTWHITE_EX}{Fore.RED}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}"
italic = f"\033[3m"
reset = f"\033[m"

print("-" * 30)
print(f"{white}ANALISADOR DE NÚMEROS INTEIROS")
print("-" * 30)

while True: # Esse é o loop principal (ele controla quando repete tudo ou fecha tudo)
    try:
        n1 = int(input("\nDigite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"{italic}Os valores digitados foram: {n1, n2}{reset}")
        if n1 > n2:
            print(f"\n{blue}O PRIMEIRO valor digitado é MAIOR")
        elif n1 < n2:
            print(f"\n{white}O SEGUNDO valor digitado é MAIOR")
        else:
            print(f"\n{white}{n1} é IGUAL a {n2}")
    except ValueError:
        print(f"\n{red}ERRO! DIGITE SOMENTE NÚMEROS")
        continue # Adicionei esse continue para que após o erro, ele volte para o loop principal, lá em cima
    while True:
        sair = str(input("\nDeseja sair? [S/N] ")).strip().lower()
        if sair == "n":
            break
        elif sair == "s":
            print("\nEncerrando...")
            for c in range(3, -1, -1):
                sleep(0.5)
                print(c)
            print(f"\n{white}PROGRAMA ENCERRADO")
            exit()
        else:
            print(f"\n{red}Erro! Digite S ou N")
