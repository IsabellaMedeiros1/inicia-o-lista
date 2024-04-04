#parte 2 do primeiro exercicio, simplificado

print("inicio programa")

lista = []

#Iterar na lista#
for i in range(5):
    print(f"Digite a sua {i+1}ª nota: ")
    n = float(input())
    lista.append(n)
print("Suas notas são: ", lista)

soma = 0
for i in range(5):
    numero = lista[i]
    soma = soma + numero
    print("Número: ", numero, "\tSoma: ", soma)
#
media = soma/5
print("Sua média é: ", media)
