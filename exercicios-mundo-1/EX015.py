#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dist = float(input("Quantos Km foram percorridos pelo carro? "))
dias = float(input("Por quantos dias o veiculo foi alugado? "))

print("O valor total a pagar é R${}. Correpondente a {} Km e {} dias".format((dist * 0.15) + (dias * 60), dist, dias))
