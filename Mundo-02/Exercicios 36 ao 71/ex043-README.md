Nesse programa criei essa valor: largura = 60 # Define 20 * 3 o valor da linha, para mais abaixo centralizar tudo, e usei dentro do print: print(f"{white}{'CALCULADORA DE IMC'.center(largura)}")
Dessa forma, consigo centralizar tudo ao invés de dar espaços manuais.
Também usei um valor para imprimir essa parte: tabela = """
TABELA OFICIAL (ABESO/OMS):
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade Mórbida."""
Até então não tinha feita dessa forma, achei legal - preciso praticar mais.
Também usei de novo essa parte aqui: for l in tabela.split("\n"): # Centraliza tudo linha por linha
    print(l.center(largura))
Dessa forma, consegui centralizar tudo linha por linha do valor criar ali em cima sobre a tabela oficial OMS.
Estava tendo problemas em criar o último loop com while True, mas percebi que não havia criado um while True inicial, para ter para onde voltar e conectar o loop debaixo (o de saída).
Demorei umas 2 horas para fazer isso dar certo, e com a ajuda do Google Mode AI.
No final, gostei do resultado - embora ainda precise praticar muito para evoluir para um próximo passo.
