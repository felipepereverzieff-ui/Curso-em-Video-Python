Nesse programa usei o nota1 separado do nota2, para validar cada número, e avançar somente quando o valor digitado for o correto pedido pelo enunciado.
Se eu fizesse ambos juntos, ao digitar o segundo número errado, ele voltaria para o número 1. Seguindo essa lógica, se tivessem vários números a serem pedidos, se tornaria exaustivo por tudo de novo por ter errado somente 1.
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
Essa foi a parte onde inovei usando o if 0 <= nota <= 10: break, para validar os números sem erro e o code ficar mais limpo, por assim dizer.
Estou testando as cores e tenho achado muito interessante como dá para fazer bastante coisas dentro do python.
Uso um Mac Air M1.
