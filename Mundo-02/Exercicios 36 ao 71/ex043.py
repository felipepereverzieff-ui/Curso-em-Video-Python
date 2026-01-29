"""Aqui vou desenvolver uma lógica que vai ler o peso e a altura de uma pessoa, calcular o seu IMC e mostrar o seu
status, segundo a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade mórbida."""

from time import sleep
from colorama import Back, Fore, Style, init
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

largura = 60 # Define 20 * 3 o valor da linha, para mais abaixo centralizar tudo

linha()
print(f"{white}{'CALCULADORA DE IMC'.center(largura)}")
linha()
tabela = """
TABELA OFICIAL (ABESO/OMS):
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade Mórbida."""

for l in tabela.split("\n"): # Centraliza tudo linha por linha
    print(l.center(largura))
print("")
linha()

while True:
    while True: # Loop para validar o peso
        try:
            peso = float(input("\nDigite o seu peso em KG (Ex.: 80): "))
            if 25 <= peso <= 250:
                break # Sai do loop se o peso for válido
            print(f"\n{red}PESO INVÁLIDO! PESO MÍNIMO: 25KG | MÁXIMO: 250KG")
        except ValueError:
            print(f"\n{red}ERRO! DIGITE SOMENTE NÚMEROS.")

    while True: # Loop para validar a altura
        try:
            altura = float(input("\nDigite sua altura (Ex.: 1.80): "))
            if 1.25 <= altura <= 2.25:
                break # Sai do loop se a altura for válida
            print(f"\n{red}ALTURA INVÁLIDA! MÍNIMO: 1.25M | MÁXIMO: 2.25M")
        except ValueError:
            print(f"{red}ERRO! DIGITE SOMENTE NÚMEROS.")

    imc = peso / (altura ** 2) # Cálculo e exibição
    print(f"\nPeso: {peso}kg\nAltura: {altura}m\nIMC: {imc:.2f}")
    status_msg = "" # Criando variável para o programa não dar erro na variável a partir daqui

    # Tabela oficial (ABESO/OMS)
    if imc < 18.5:
        status_msg = f"{cyan}ABAIXO DO PESO"
    elif imc < 25:
        status_msg = f"{green}PESO IDEAL"
    elif imc < 30:
        status_msg = f"{blue}SOBREPESO"
    elif imc < 40:
        status_msg = f"{yellow}OBESIDADE"
    else:
        status_msg = f"{red}OBESIDADE MÓRBIDA"
    print(f"\nResultado: {status_msg}")

    while True: # Loop de saída
            sair = str(input("\nDeseja sair? [S/N]: ")).strip().lower()
            if sair == "s":
                print("Saindo...")
                for c in range(3, -1, -1):
                    print(c)
                    sleep(0.3)
                print(f"\n{white}PROGRAMA ENCERRADO!")
                exit()
            elif sair == "n":
                break
            else:
                print(f"\n{red}ERRO! DIGITE S OU N.")
