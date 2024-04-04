#lista []
#lista 1 = list()
#indices  0  1  2
lista1 = [7, 6, 9]
print(lista1[1]) #colocar sem o valor (variavel) vai mostrar a lista inteira

lista1.append(8) 
#a lista vai ficar [7, 6. 9, 8]
#indice             0, 1, 2, 3

print("___________________________________")

lista2 = [7, 10, 8, 4]
lista2[2] = 8.5 #mudar algo da lista
print("Lista dps de mudar um valor: ", lista2)

print("___________________________________")
lista3 = [6, 7, 8]
print("Lista dps de remover:", lista3)
lista3.pop(1)
