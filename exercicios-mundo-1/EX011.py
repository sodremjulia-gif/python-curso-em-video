#"Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2 metros quadrados."

larg = float(input("Informe as medidas da parede que será pintada. Qual a largura? "))
altu = float(input("E qual a altura? "))
rend_tinta = float(input("(Referente a 1 litro) Qual o rendimento dessa tinta?  "))
q_tinta = (larg * altu) / rend_tinta

print("Para pintar essa parede voce precisará de {:.1f} litros de tinta".format(q_tinta))
