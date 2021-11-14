parcelas = 0
totalDebito = int(input())
valorPagoMensal = int(input())
faltaPagar = 0
while totalDebito != 0:
    if totalDebito > valorPagoMensal:
        parcelas += 1
        print(f'pagamento: {parcelas}')
        print(f'antes = {totalDebito}')
        totalDebito = totalDebito - valorPagoMensal
        print(f'depois = {totalDebito}')
        print('-' * 5)
    else:
        parcelas += 1
        print(f'pagamento: {parcelas}')
        print(f'antes = {totalDebito}')
        print('depois = 0')
        print('-' * 5)
        break