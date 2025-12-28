"""num = int(input{"Ingresar numeros"})"""

for i in range(num):
num_usuario = int(input{"Ingresar numeros:"})
lista_de_numeros.append(num_usuario)

lista_ordenada = sorted(lista_de_numeros, reverse=True)
print(lista_de_numeros)
print(lista_ordenada)