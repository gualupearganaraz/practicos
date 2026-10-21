from collections import deque


def por_niveles(arbol, g):
    if not arbol or arbol[0] is None:
        return

    cola = deque([0])

    while cola:
        i = cola.popleft()
        print(arbol[i])

        for j in range(1, g + 1):
            hijo = g * i + j

            if hijo < len(arbol) and arbol[hijo] is not None:
                cola.append(hijo)


def main():
    arbol = ["A", "B", "C", "D", "E", "F", "G"]
    grado = 2

    print("Barrido por niveles:")
    por_niveles(arbol, grado)


if __name__ == "__main__":
    main()
