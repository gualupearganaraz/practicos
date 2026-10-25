import sys


def leer_arbol(nombre_archivo):
    arbol = []
    archivo = open(nombre_archivo)
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            arbol.append(int(linea))
    archivo.close()
    return arbol


def simetrico(arbol, i):
    # TODO: tu algoritmo
    # Imprimí cada nodo con print(arbol[...]), uno por renglón
    pass


def main():
    nombre_archivo = sys.argv[1]       
    arbol = leer_arbol(nombre_archivo)
    simetrico(arbol, 0)              

if __name__ == "__main__":
    main()
