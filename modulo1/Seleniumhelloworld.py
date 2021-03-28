def indice(string1: str):
    for i in range(len(string1)):
        indi = string1.find(string1[i])
        if indi:
            print(indi)

    print(-1)


cadena = str(input("Escribe una cadena de texto: "))
indice(cadena)
