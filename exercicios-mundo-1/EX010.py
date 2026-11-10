#" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."
din = float(input("Quantos reais ha em sua carteira? "))
dolar = float(input("Qual a cotação do dolar hoje? "))
print("Com R${} voce pode comprar US${:.2f}".format(din,din/dolar ))
