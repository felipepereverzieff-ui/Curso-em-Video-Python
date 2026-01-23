"""Aqui vou refazer o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes"""

from time import sleep
from colorama import init, Back, Fore, Style

init(autoreset=True)

# Cores que sempre uso nos codes, então vão ter cores aqui que podem não serem usadas nesse programa
blue = f"{Back.LIGHTWHITE_EX}{Fore.BLUE}{Style.BRIGHT}"
yellow = f"{Back.LIGHTWHITE_EX}{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Back.LIGHTWHITE_EX}{Fore.RED}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}"
green = f"{Back.LIGHTWHITE_EX}{Fore.GREEN}{Style.BRIGHT}"
cyan = f"{Back.LIGHTWHITE_EX}{Fore.CYAN}{Style.BRIGHT}"
yellow_background = f"{Back.YELLOW}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}"
black_background = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}"

def linha():
    print("-=-" * 20)

print("-=-" * 20)
print("\033[7mANALISADOR DE TRIÂNGULOS AVANÇADO\033[m")
print("\033[7mDICA: NÃO EXISTEM TRIÂNGULOS COM VALORES NEGATIVOS\033[m") # Aqui pus a dica para o user não digitar nenhum número negativo

while True: # Loop principal
    try:
        linha()
        r1 = float(input("\nDigite o primeiro segmento: "))
        r2 = float(input("Digite o segundo segmento: "))
        r3 = float(input("Digite o terceiro segmento: "))
        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # Cálculo para ver se é triângulo ou não
            print("\nOs segmentos digitados podem formar um triângulo:")
            if r1 == r2 == r3:
                print(f"{white}EQUILÁTERO")
                print(" ")
            elif r1 == r2 or r1 == r3 or r2 == r3:
                print(f"{blue}ISÓSCELES")
            else:
                print(f"{yellow}ESCALENO")
        else:
            print(f"\n{red}Os segmentos digitados não podem formar um triângulo.")
    except ValueError:
        print(f"{red}ERRO! DIGITE UM VALOR VÁLIDO.")
        continue # Volta ao Loop principal
    while True:
        sair = str(input("\nDeseja sair? [S/N] ")).strip().lower()
        if sair == "n":
            break
        elif sair == "s":
            print("Saindo...")
            for c in range(3, -1, -1):
                sleep(0.3)
                print(f"{c}...", end=" ")
            print(f"\n{black_background}FINALIZADO")
            exit() # Sai de vez do programa
        else:
            print(f"{red}ERRO! DIGITE S OU N.")
