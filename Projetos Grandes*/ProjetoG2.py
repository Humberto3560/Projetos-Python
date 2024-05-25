cont1 = 1
cont2 = 1
soma = 0
multiplicacao = 0

while cont1 > 0:
    while cont2 > 0:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))

        print("""Digite uma opção:
        [1] Somar
        [2] Multiplicar
        [3] Comparar
        [4] Novos números
        [5] Fechar programa
        """)
        numero = int(input("Escolha sua opção: "))
        if numero == 1:
            print("Opção 1 escolhida")
            soma = n1 + n2
            print("Resultado da soma:", soma)
            print("""


            """)
        elif numero == 2:
            print("Opção 2 escolhida")
            multiplicacao = n1 * n2
            print("Resultado da multiplicação:", multiplicacao)
            print("""


            """)
        elif numero == 3:
            print("Opção 3 escolhida")
            if n1 == n2:
                print("Ambos são iguais")
            elif n1 > n2:
                print("O primeiro número é maior que o segundo")
            else:
                print("O segundo número é maior que o primeiro")
                print("""


                """)
        elif numero == 4:
            print("Opção 4 escolhida")
            # Aqui você pode reiniciar as variáveis n1, n2, soma e multiplicacao se necessário
            n1 = 0
            n2 = 0
            soma = 0
            multiplicacao = 0
            print("""


            """)
        elif numero == 5:
            print("Fechando o programa...")
            cont1 = 0  # Alterando o valor de cont1 para sair do primeiro loop
            cont2 = 0  # Alterando o valor de cont2 para sair do segundo loop
            print("""


            """)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
