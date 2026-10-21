def postorden(arbol, g, i=0):
    if i >= len(arbol) or arbol[i] is None:
        return

    for j in range(1, g + 1):
        hijo = g * i + j
        postorden(arbol, g, hijo)

    print(arbol[i])


def main():
    arbol = ["A", "B", "C", "D", "E", "F", "G"]
    grado = 2

    print("Barrido postorden:")
    postorden(arbol, grado)


if __name__ == "__main__":
    main()
