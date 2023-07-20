

menu = f"""
{'-'.center(60, '-')}
        MENU

    [1] Saque
    [2] Depósito
    [3] Visualizar extrato
    [4] Sair

"""

saldo = 1000
limite_saque = 3
SAQUE_MAXIMO = 500.00
extrato = ''

repeticao = True
while repeticao:
    print(menu)
    opcao = input('Qual operação deseja fazer? ').strip()
    if opcao.isnumeric() is False:
        print('Você não digitou um número')
        continue
    elif int(opcao) > 4:
        print('Você digitou um número diferente das opções')
        continue
    else:
        if opcao == '1':
            if limite_saque != 0:
                saque = input('[LIMITE DE R$500,00]Quanto você deseja sacar? ').strip()
                if saque.isnumeric() is True:
                    saque = float(saque)
                    if saque > SAQUE_MAXIMO:
                        print('Você não pode sacar valor acima de R$500,00')
                    else:
                        saldo -= saque
                        limite_saque -= 1
                        extrato = extrato + f'-R${str(saque)} saldo=R${str(saldo)} | '
                else:
                    print('Você precisa digitar um número!')
            else:
                print('VOCÊ ATINGIU O LIMITE DE SAQUE')
                break
        elif opcao == '2':
            deposito = input('Quanto você deseja depositar? ').strip()
            if deposito.isnumeric() is False:
                print('Você deve digitar um número!')
            else:
                saldo += float(deposito)
                extrato = extrato + f'+R${deposito} saldo=R${saldo} | '
        elif opcao == '3':
            if extrato == '':
                print('Seu extrato está vazio.')
            else:
                print(extrato)
        elif opcao == '4':
            break

print('Obrigado por usar!')

        


