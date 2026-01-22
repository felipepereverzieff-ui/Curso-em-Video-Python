"""Aqui vou criar um programa que vai ler duas notas de um aluno e calcular sua média, mostrando uma mensagem no final,
de acordo com a média atingida.
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

from time import sleep
from colorama import Back, Fore, init, Style

init(autoreset=True)

def linha():
    print("-=-" * 20)

# Cores
blue = f"{Back.LIGHTWHITE_EX}{Fore.BLUE}{Style.BRIGHT}"
yellow = f"{Back.LIGHTWHITE_EX}{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Back.LIGHTWHITE_EX}{Fore.RED}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}"
green = f"{Back.LIGHTWHITE_EX}{Fore.GREEN}{Style.BRIGHT}"
cyan = f"{Back.LIGHTWHITE_EX}{Fore.CYAN}{Style.BRIGHT}"
yellow_background = f"{Back.YELLOW}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}"
black_background = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}"

linha()
print(f"{white}CALCULADORA DE MÉDIA")
linha()
print(f"{black_background}SERÁ QUE VOCÊ PASSOU DE ANO, FICOU DE RECUPERAÇÃO, OU REPROVOU?")
linha()
print("TABELA DE MÉDIAS:"
      "\n- Média abaixo de 5.0: REPROVADO"
      "\n- Média entre 5.0 e 6.9: RECUPERAÇÃO"
      "\n- Média 7.0 ou superior: APROVADO")
linha()


while True:

    while True: # Validaremos a nota1 aqui
        try:
            nota1 = float(input(f"\n{black_background}Digite a primeira nota: "))
            if 0 <= nota1 <= 10:
                break # Só sairemos desse loop se a nota for válida
            print(f"{red}ERRO! DIGITE NOTAS DE 0 A 10 SOMENTE")

        except ValueError:
            print(f"{red}ERRO! DIGITE UM NÚMERO VÁLIDO")

    while True: # Validaremos a nota2 aqui
        try:
            nota2 = float(input(f"\n{black_background}Digite a segunda nota: "))
            if 0 <= nota2 <= 10:
                break # Só sairemos desse loop se a nota for válida
            print(f"\n{red}ERRO! DIGITE NOTAS DE 0 A 10 SOMENTE")

        except ValueError:
            print(f"{red}ERRO! DIGITE NOTAS DE 0 A 10 SOMENTE")

    media = (nota1 + nota2) / 2
    if media < 5:
        print(f"\n{red}Você está REPROVADO. Sua média foi: {media:.1f}")
    elif 5 <= media <= 6.9:
        print(f"\n{yellow}Você está de RECUPERAÇÃO. Sua média foi: {media:.1f}")
    else:
        print(f"\n{green}Parabéns, você está APROVADO! Sua média foi: {media:.1f}")

    while True: # Aqui daremos a opção da pessoa sair do programa
        sair = str(input(f"\n{blue}Deseja sair? [S/N] ")).strip().lower()
        if sair == "n":
            break
        if sair == "s":
            print("\nSaindo do sistema...")
            for c in range(3, -1, -1):
                sleep(0.3)
                print(c)
            print(f"\n{white}PROGRAMA ENCERRADO")
            exit()
        else:
            print(f"\n{red}ERRO! DIGITE S OU N")



