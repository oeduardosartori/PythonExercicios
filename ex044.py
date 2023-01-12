"""Elabora um programa que calcule o valor a ser pago por um produto, conciderando o seu preço normal e condição de
pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros"""
print('\033[1;34;40m=' * 10, 'LOJA DO ZÉ', '=' * 10, '\033[m')
valor = float(input('Preço da compra: R$ '))
print('\033[1;30;44mFORMA DE PAGAMENTO\033[m')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Em até 2x no cartão')
print('[ 4 ] 3x à 12 x no cartão de crédito')
opcao = int(input('Qual a opção de pagamento: '))

pay1 = valor - (valor * 0.10)
pay2 = valor - (valor * 0.05)
pay3 = valor
pay4 = valor + (valor * 0.20)

if opcao == 1:
    print('Você ganhará um desconto de 10% por escolher o pagamento à vista no dinheiro ou cheque.')
    print(f'Sua compra de R$ {valor} vai custar R$ {pay1:.2f} no final!')
elif opcao == 2:
    print('Você ganhará um desconto de 5% por escolher o pagamento à vista no cartão.')
    print(f'Sua compra de R$ {valor} vai custar R$ {pay2:.2f} no final!')
elif opcao == 3:
    print('Você escolheu pagar em 2X no cartão, então o preço da compra continuará o mesmo sem juros.')
    print(f'Sua compra de R$ {valor} vai custar R$ {pay3:.2f} no final!')
elif opcao == 4:
    print('Você escolheu pagar a cima de 3X no cartão, sendo assim o valor final terá um acréscimo de 20% de juros.')
    print(f'Sua compra de R$ {valor} vai custar R${pay4:.2f} no final!')
else:
    print('Não possuimos esta opção!\nEscolha entre 1,2, 3 e 4.')
