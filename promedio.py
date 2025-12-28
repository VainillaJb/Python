# Esta funcion abre el archivo con los estudiantes y regresa una list de strings
def leer_informacion_estudiantes():
    nombre_archivo_datos = 'estudiantes.txt'
    lista_estudiantes = []
    # Open file
    with open(nombre_archivo_datos) as file:
        lineas = file.readlines()
        for linea in lineas:
            atributos_estudiante = linea.split(', ')
            # Eliminar character de nueva linea
            atributos_estudiante[-1] = atributos_estudiante[-1][:-1]
            lista_estudiantes.append(atributos_estudiante)
    return lista_estudiantes

class Estudiante:
    def __init__(self, datos):
        self.id = datos[0]
        self.apellido = datos[1]
        self.nombre = datos[2]
        self.correo = datos[3]
        self.notas = [float(n) for n in datos[4:]]

    def promedio(self):
        """# TODO
        # Completa esta funcion para que retorne el promedio de un estudiante"""
        if not self.notas:
            return 0.0
        """return 10"""
        return sum(self.notas) / len(self.notas)

    def estado(self):
        return "Aprueba" if self.promedio() > 7 else "No aprueba"
        
    def __lt__(self, other):
        return self.promedio() > other.promedio()
    
    def __str__(self):
        return f"{self.id} {self.apellido} {self.nombre} {self.correo} {self.promedio():.4f} {self.estado()}"

"""datos_estudiantes = leer_informacion_estudiantes()
for datos_estudiante in datos_estudiantes:
    print('Datos de estudiante', datos_estudiante)"""

datos_crudos = leer_informacion_estudiantes()

lista_objetos_estudiantes = []
for datos in datos_crudos:
    nuevo_estudiante = estudiante(datos)
    lista_objetos_estudiantes.append(nuevo_estudiante)
    
estudiantes_ordenados = sorted(lista_objetos_estudiantes)

print("ID | Apellido | Nombre | Correo | Promedio | Resultado")
for est in estudiantes_ordenados:
    print(est)


# Aqui deberas asegurarte que la lista de de estudiantes sea ordenada
# TODO

# Aqui deberas imprimir cada uno de los estudiantes
# ya que han sido ordenados
# TODO
