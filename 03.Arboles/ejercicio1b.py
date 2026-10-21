def preorden(arbol, g, i=0):
    if i >= len(arbol):
        return

    print(arbol[i])

    for j in range(1, g + 1):
        hijo = g * i + j
        preorden(arbol, g, hijo)


def main():
    arbol = ["A", "B", "C", "D", "E", "F", "G"]
    grado = 2

    print("Barrido preorden:")
    preorden(arbol, grado)


if __name__ == "__main__":
    main()
