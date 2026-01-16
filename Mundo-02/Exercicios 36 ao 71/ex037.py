"""Aqui farei um programa que vai ler um número inteiro qualquer e pedir para o user escolher qual será a base
de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""
from time import sleep
print("*" * 40)
print(" \033[7mCONVERSOR BINÁRIO, OCTAL E HEXADECIMAL\033[m")
print("*" * 40)
while True:
    try:
        entrada = int(input("\nDigite um número inteiro qualquer: "))
        print(f"\nVocê gostaria de converter o número [{entrada}] digitado para: ")
        print("[1] Binário")
        print("[2] Octal")
        print("[3] Hexadecimal")
        escolha_do_user = int(input("\nDigite sua escolha: "))
        if escolha_do_user == 1:
            print(f"\033[33;1;3m[{entrada}] em binário: {bin(entrada)[2:].upper()}\033[m")
        elif escolha_do_user == 2:
            print(f"\033[34;1;3m[{entrada}] em octal: {oct(entrada)[2:].upper()}\033[m")
        elif escolha_do_user == 3:
            print(f"\033[35;1;3m[{entrada}] em hexadecimal: {hex(entrada)[2:].upper()}\033[m")
        else:
            print("\033[31;1mERRO! DIGITE 1, 2 OU 3.\033[m")
            continue
    except ValueError:
        print("\033[31;1mERRO! LEIA O ENUNCIADO NOVAMENTE.\033[m")
        continue
    while True:
        sair = str(input("\nDeseja sair do conversor? [S/N] ")).strip().lower()
        if sair == "s":
            print("Encerrando o conversor...")
            for c in range(3, -1, -1):
                sleep(0.5)
                print(c)
            print("\033[7mCONVERSOR ENCERRADO\033[m")
            exit()
        elif sair == "n":
            break
        else:
            print("\033[31;1mERRO! DIGITE S OU N.\033[m")
