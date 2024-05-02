MENU = ("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
""")

saldo = 500
limite = 500
extrato = ''
limite_para_saque = 3
numero_saques = 0  # Adicionado para manter o controle do número de saques

while True:
    opcao = input(MENU)
    if opcao == "1":
        valor = float(input("Digite um valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R${valor:.2f}\n"
        else:
            print("Operação sem sucesso. O valor informado não é válido.")

    elif opcao == "2":
        if numero_saques >= limite_para_saque:
            print(f"Sem sucesso na operação, número máximo de tentativas no seu limite é {limite_para_saque}.")
            continue

        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Sem sucesso na operação, saldo insuficiente. O saldo é:", saldo)
        elif valor > limite:
            print("Sem sucesso na operação. O valor para sacar excede o limite permitido, seu limite é: ", limite)
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação sem sucesso. O valor informado não é válido.")

    elif opcao == "3":
        if extrato:
            print("Extrato dos movimentos:")
            print(extrato)
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Não foram realizados movimentos. Sem nenhum extrato.")

    elif opcao == "4":
        print("Saindo do programa!")
        break

    else:
        print("Operação inválida. Selecione outra opção!")
