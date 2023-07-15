#sistema bancario

menu = """


[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("INFORME O VALOR DO DEPÓSITO: "))

        if valor > 0:
            saldo+= valor
            extrato+= f"Depósito: R$ {valor:.2f}\n"
        

            
        else:
            print("OPERAÇÃO FALHOU! O VALOR INFORMADO É VÁLIDO")    


    elif opcao == "2":
        valor = float(input("INFORME O VALOR DE SAQUE: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("OPERAÇÃO FALHOU! VOCÊ NÃO TEM SALDO SUFICIENTE!")

        elif excedeu_limite :
            print("OPERAÇÃO FALHOU! EXCEDEU O LIMITE DE SAQUE")

        elif excedeu_saques:
            print("OPERAÇÃO FALHOU! NÚMERO DE SAQUE EXCEDIDO") 

        elif valor>0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques +=1

        else:
            print("OPERAÇÃO FALHOU ! O VALOR INFORMADO É INVÁLIDO!")  
             

    elif opcao == "3":
        print("\n========EXTRATO========")
        print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
        print(f"n\saldo: R${saldo:.2f}")
        print("=========================") 

    elif opcao =="4":
        break

    else:
        print("Operção inválida!\n" "Por favor selecione a opção desejada.")
                  