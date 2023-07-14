
quantidade_saques = 0
extrato = ""
saldo = 0
LIMITE_SAQUES = 3

while True:
    
    print("\nBem vindo!")   

    print(f"""          
        -------------------
        Informações úteis: 
        Você já usou {quantidade_saques} dos 3 saques disponíveis no dia!
        Lembre-se que você pode sacar no máximo R$ 500,00 por operação.
        ------------------
        """
    )     

    opcao = input("""
        Escolha uma das opções a seguir: 

        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Sair
        
        Opção escolhida:
        """
        )

    if int(opcao) == 1:
        valor_do_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            extrato += f"Depósito: R$ {valor_do_deposito:.2f}\n"
            print(f"""
                  
                  -----------------
                  Você acabou de depositar R$ {valor_do_deposito}!
                  Fim de execução.
                  -----------------

                  """)
        else:
            print("O valor que você digitou não é permitido, informe um valor maior que zero.")
            

    elif int(opcao) == 2:
        if quantidade_saques < 3:
            valor_do_saque = float(input("Informe o valor do saque: "))

            if valor_do_saque > 0 and valor_do_saque <= 500:
                if valor_do_saque <= saldo:
                    saldo -= valor_do_saque
                    extrato +=  f"Saque: R$ {valor_do_saque:.2f}\n"
                    quantidade_saques += 1
                    print(f"""
                            
                          -----------------
                          Você acabou de sacar R$ {valor_do_saque}!
                          Quantidade de saques: {quantidade_saques} de 3
                          Fim de execução.
                          -----------------

                        """)

                else:
                    print("Seu saldo é insuficiente para essa operação!")
                    

            elif valor_do_saque > 500:
                print("Valor solicitado excede o limite por operação!")
                
            else:
                print("Você digitou um valor inválido, tente novamente.")
                
        else:
            print("Você já atingiu a quantidade máxima de saques do dia. Tente novamente amanhã!")
            
    elif int(opcao) == 3:
        print("\n-------------------Extrato-----------------\n")
        print("\nSem movimentações!!" if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("\n-----------------Fim do Extrato---------------")

    elif int(opcao) == 4:
        print("Obrigada por usar nossos serviços!")
        break

    else:
        print("Opção inválida, selecione novamente a opção desejada!")

    