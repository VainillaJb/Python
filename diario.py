import os
from datetime import datetime

def diario():
    if not os.path.exists('diario_entradas'):
        os.mkdir('diario_entradas')

def manejar_accion_escribir():
    ahora = datetime.now()
    nombre_archivo = ahora.strftime("%Y_%M_%d_%H_%M_%S") + ".txt" [cite: 27, 29]
    ruta = os.path.join(diario_entradas, nombre_archivo)

    print(f"La nueva entrada usara la siguiente fecha y hora: {nombre_archivo[:-4]}") [cite: 31]
    print("Por favor escribe el dato para dejar espacio") [cite: 32]

    lineas = []
    blanco_cons = 0

#BUCLE WHITE

while blanco_cons < 3:
    lineas = input()
    if lineas.strip() == "":
        blanco_cons += 1
    else
        blanco_cons = 0
    linea.append(lineas)


#GUARDAR

with open(ruta, "w") as archvo:
    archvo.write("\n".join(linea))
print("Entrada guardada con exito.")


def manejar_accion_leer():
    archivos = os.listdir(diario_entradas)

    if not archivos