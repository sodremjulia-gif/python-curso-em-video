#"Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."
n = int(input("Digite um numero: "))
dobro = n * 2
triplo = n * 3
raiz = n **0.5

print("O dobro é {}, e o triplo é {}. \nA raiz quadrada é {:.2f}".format(dobro, triplo, raiz))
