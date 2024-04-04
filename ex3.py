'''
Utilizando as ténicas para popular listas e somar
valores da lista, crie um programa para calcular
a media de crescimento anual de uma planta. Para isto
o programa deverá pedir a altura da planta medida na
semana, por 10 semanas. Com base na soma destas alturas
calcule a média de crescimento ao longo das semanas.
'''

print("inicio programa")
qtd_mes = 3
crescimento = []

for i in range(qtd_mes):
    print(f"Por favor informe o crescimento do mes {i +1}")
    cres_mes = float(input())
    crescimento.append(cres_mes)

soma = 0
for i in range(qtd_mes):
    soma = soma + crescimento[i]

media = soma /qtd_mes
print("Esta é a média de crescimento mesnsal da planta: ", media)
