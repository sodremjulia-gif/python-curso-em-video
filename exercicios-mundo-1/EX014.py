#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
temp = float(input("""Conversão de celsius para fahrenheit.
Digite a temperatura que deseja converter: """))

print("A temperatura {}°C correponde a {:.1f}°F".format(temp, (temp*1.8)+32))
