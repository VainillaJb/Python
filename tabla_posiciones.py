# 1. Primero creamos la lista vacía (esto te faltaba)
lequipo = []

numero_equipos = input("numero equipos: ")
numero_equipos = int(numero_equipos)

for i in range(numero_equipos):
    # CORRECCIÓN: Usamos "=" para asignar el nombre
    equipo = input(f"Nombre equipo {i+1}: ") 
    
    # Agregamos el nombre a la lista
    lequipo.append(equipo)

# Esto imprimirá la lista de nombres al final
print("\nLos equipos ingresados son:")
print(lequipo)