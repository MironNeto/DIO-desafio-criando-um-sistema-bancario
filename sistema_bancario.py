
menu = """
Escolha a sua operacao desejada:

[d] = depositar
[s] = sacar
[e] = extrato
[q] = sair
"""

saldo = 0
extrato = "______________EXTRATO______________\n\n"
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
VALOR_LIMITE_SAQUE = 500

while True:
    
    opcao = input(menu)

    if opcao == "d":
        mensagem = """
Opcao deposito selecionada.
Digite o valor que voce deseja depositar.
"""
        valor_deposito = float(input(mensagem))
        saldo += valor_deposito

        extrato += f'Deposito  -------------    R$ {valor_deposito:.2f}\n'
        print(f"Depositado valor de R$ {valor_deposito:.2f} na conta.")
        
    elif opcao == "s":        
        mensagem = """
Opcao  saque selecionada.
Digite o valor que voce deseja sacar.
"""
        valor_saque = float(input(mensagem))

        if valor_saque > VALOR_LIMITE_SAQUE:
            print("Valor solicitado esta acima do valor limite por saque.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        elif numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite de saques diarios atingido")
        else:
            saldo -= valor_saque
            numero_saques += 1
            
            extrato += f'Saque     -------------    R$ {valor_saque:.2f}\n'
            print(f'Saque realizado no valor de R$ {valor_saque:.2f}')


    elif opcao == "e":
        print("Opcao extrato selecionada.\n\n")
        print(extrato)
    elif opcao == "q":
        print("Opcao sair selecionada.")
        break
    else:
        print("Opcao selecionada e invalida. Por favor, selecione novamente a operacao desejada.")