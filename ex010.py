# Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar.
# Considere - US$ 1.00 == R$ 3.27
dinheiro = float(input('Quanto dinheiro você tem em sua carteira? R$ '))
print(f'Com R$ {dinheiro}, você pode comprar US${dinheiro / 3.27:.2f}')
