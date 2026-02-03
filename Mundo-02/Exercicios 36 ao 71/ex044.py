"""Aqui vou criar um programa que vai calcular o valor a ser pago por um produto, considerando o seu preço normal,
e condição de pagamento:
- À vista (dinheiro/PIX): 10% de desconto
- À vista no cartão: 5% de desconto
- Em 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros"""

from time import sleep
from colorama import init, Back, Fore, Style
init(autoreset=True)

red = f"{Back.LIGHTWHITE_EX}{Fore.RED}{Style.BRIGHT}"
white = f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}"

def linha():
    print("-=-" * 20)

while True:
    while True:
        try:
            linha()
            entrada = float(input(f"{white}Digite o valor total da sua compra: R$"))
            if entrada <= 0:
                print(f"{red}Erro! Não digite valores negativos.")
                continue
            break
        except ValueError:
            print(f"\n{red}Erro! Digite somente números.")
    print("""\nComo você gostaria de pagar?
\n[1] À vista (dinheiro/PIX): 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em 2x no cartão: preço normal sem juros
[4] Em 3x ou mais no cartão: 20% de juros""")
    while True:
        try:
            escolha = int(input(f"\n{white}Digite a sua escolha: "))
            if escolha == 1:
                desconto = entrada - (entrada * 0.10)
                print(f"O preço final da sua compra é: R${desconto:.2f}")
            elif escolha == 2:
                desconto = entrada - (entrada * 0.05)
                print(f"O preço final da sua compra é: R${desconto:.2f}")
            elif escolha == 3:
                parcela = entrada / 2
                print(f"Sua compra será parcelada em 2x de R${parcela:.2f}.")
            elif escolha == 4:
                while True:
                    try:
                        total = entrada + (entrada * 0.20)
                        totalparcelas = int(input(f"\n{white}Quantas parcelas? "))
                        if totalparcelas < 3:
                            print(f"\n{red}Erro! Essa opção só aceita 3x ou mais.")
                            continue
                        break
                    except ValueError:
                        print(f"\n{red}Erro! Digite um número válido para as parcelas.")
                parcela = total / totalparcelas
                print(f"Sua compra será parcelada em {totalparcelas}x de R${parcela:.2f}")
                print(f"O total da compra em {totalparcelas}x com 20% de juros vai ser de R${total:.2f}")
            else:
                print(f"\n{red}Erro! Opção inválida de pagamento.")
                continue
            break
        except ValueError:
            print(f"\n{red}Erro! Digite a sua escolha (1 ao 4).")
            continue
    while True:
        sair = str(input(f"\n{white}Deseja sair? [S/N]")).strip().lower()
        if sair == "n":
            break
        elif sair == "s":
            print("Saindo...")
            for c in range(3, -1, -1):
                print(c)
                sleep(0.5)
            print("Até a próxima!")
            exit()
        else:
            print(f"\n{red}Erro! Digite S ou N.")
