#programa que leia algo pelo teclado e mostre na tela o seu tipo ptimitivo e todas as informações possiveis sobre ela
v=input("Digite algo: ")
print("O tipo primitivo desse valor é", type(v))
print("Só tem espaços?", v.isspace())
print("É um número?", v.isnumeric())
print("É alfabetico?", v.isalpha())
print("É um alfanumérico?", v.isalnum())
print("Esta em minusculas?", v.islower())
print("Esta em maiusculas?", v.isupper())
print("Esta capitalizado?", v.istitle())
#metodos do objeto "v"
