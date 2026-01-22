"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM (0 a 9)
- Até 14 anos: INFANTIL (10 a 14)
- Até 19 anos: JUNIOR (15 a 19)
- Até 25 anos: SÊNIOR (20 a 25)
- Acima: MASTER. (26 ou mais)"""

from time import sleep # Uso para dar uma UX melhor
from datetime import date # Uso esse para puxar a data atual ao invés de fazer um programa com ano fixo
from colorama import init, Back, Fore, Style # Uso para melhorar as cores e usá-las de forma mais simples

init(autoreset=True) # Reseta as cores no final da linha

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
    # Aqui defino uma linha ao invés de ficar digitando 1 milhão de print dentro do código
    print("-=-" * 20)
while True: # Aqui é o loop principal
    try:
        data_atual = date.today().year # Essa puxa a data atual para fazer os cálculos dentro do code
        linha()
        ano_de_nascimento = int(input("Qual o ano de nascimento do atleta? "))
        idade = data_atual - ano_de_nascimento # Calcula a idade do atleta para calcular os if/elif
        if not 0 <= idade <= 120: # Aqui se a idade não estiver dentro de 0 a 120, o programa repete o loop
            print(f"\n{red}ERRO! ANO INVÁLIDO.")
            continue
    except ValueError: # Aqui tratamos erros ao digitar algo que não seja números
            print(f"\n{red}ERRO! DIGITE UM NÚMERO VÁLIDO.")
            continue
    print(f"\nNesse ano de {data_atual}, o atleta tem ou terá {idade} anos.")
    if idade <= 9:
        print("\nCategoria: MIRIM")
    elif idade <= 14:
        print("\nCategoria: INFANTIL")
    elif idade <= 19:
        print("\nCategoria: JUNIOR")
    elif idade <= 25:
        print("\nCategoria: SÊNIOR")
    else:
        print("\nCategoria: MASTER")
    while True:
        sair = str(input(f"\n{blue}Deseja sair? [S/N]")).strip().lower()
        if sair == "n":
            break
        elif sair == "s":
            print("Saindo...")
            for c in range(3, -1, -1):
                sleep(0.3)
                print(f"{c}...", end=" ")
            print(f"\n\n{white}PROGRAMA ENCERRADO!")
            exit()
        else:
            print(f"\n{red}ERRO! DIGITE S OU N.")
