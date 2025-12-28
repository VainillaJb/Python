"""def piramide(n, fila=1):
    if fila > n:
        return
    print("*" * fila)
    piramide(n, fila + 1)

num_fila = int(input("Ingrese el numero de filas: "))
piramide(num_fila)"""

def entrada_num():
    try:
        num = float(input("ingrese numeros: "))
        return num
    except ValueError:
        print("Errror ingrese un tipo de dato numerico")
entrada_num()
