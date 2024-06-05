"""Un estado será una lista con dos valores [jarra3, jarra5]
estadosVisitados será una lista de estados por los que ya se ha pasado"""

def jarras(estado, estadosVisitados, camino):
    estadosVisitados.append([estado[0], estado[1]])
    if estado[0] + estado[1] == 7:
        print(camino)
    else:
        """Llenar Jarra 3"""
        if estado[0] < 3:
            jarra3 = estado[0]
            estado[0] = 3
            if estado not in estadosVisitados:
                camino.append([estado[0], estado[1]])
                jarras(estado, estadosVisitados, camino)
                camino.remove([estado[0], estado[1]])
            estado[0] = jarra3

        """Llenar Jarra 5"""
        if estado[1] < 5:
            jarra5 = estado[1]
            estado[1] = 5
            if estado not in estadosVisitados:
                camino.append([estado[0], estado[1]])
                jarras(estado, estadosVisitados, camino)
                camino.remove([estado[0], estado[1]])
            estado[1] = jarra5

        """Vaciar Jarra 3"""
        if estado[0] > 0:
            jarra3 = estado[0]
            estado[0] = 0
            if estado not in estadosVisitados:
                camino.append([estado[0], estado[1]])
                jarras(estado, estadosVisitados, camino)
                camino.remove([estado[0], estado[1]])
            estado[0] = jarra3

        """Vaciar Jarra 5"""
        if estado[1] > 0:
            jarra5 = estado[1]
            estado[1] = 0
            if estado not in estadosVisitados:
                camino.append([estado[0], estado[1]])
                jarras(estado, estadosVisitados, camino)
                camino.remove([estado[0], estado[1]])
            estado[1] = jarra5

        """Trasbase 3 a 5"""
        jarra3 = estado[0]
        jarra5 = estado[1]
        while estado[0] > 0 and estado[1] < 5:
            estado[0] -= 1
            estado[1] += 1
        if estado not in estadosVisitados:
            camino.append([estado[0], estado[1]])
            jarras(estado, estadosVisitados, camino)
            camino.remove([estado[0], estado[1]])
        estado[0] = jarra3
        estado[1] = jarra5

        """Trasbase 5 a 3"""
        while estado[0] < 3 and estado[1] > 0:
            estado[0] += 1
            estado[1] -= 1
        if estado not in estadosVisitados:
            camino.append([estado[0], estado[1]])
            jarras(estado, estadosVisitados, camino)
            camino.remove([estado[0], estado[1]])
        estado[0] = jarra3
        estado[1] = jarra5

print("JARRAS DE AGUA\n------------------")
camino = [[0,0]]
jarras([0,0],[], camino)

"""

def encontrar_camino(laberinto, x, y, solucion, visitadas):
    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        solucion[x][y] = 2
        return True

    if len(laberinto) > x >= 0 == laberinto[x][y] and 0 <= y < len(laberinto[0]) and not visitadas[x][y]:
        solucion[x][y] = 2
        visitadas[x][y] = True

        if (encontrar_camino(laberinto, x + 1, y, solucion, visitadas)
        or encontrar_camino(laberinto, x, y + 1, solucion, visitadas)
        or encontrar_camino(laberinto, x - 1, y, solucion, visitadas)
        or encontrar_camino(laberinto, x, y - 1, solucion, visitadas)):
            return True

        solucion[x][y] = 0

    return False


print("\n\nLABERINTO\n------------------")
laberinto = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

solucion = [row[:] for row in laberinto]
visitadas = [[False] * len(laberinto[0]) for _ in range(len(laberinto))]

if encontrar_camino(laberinto, 0, 0, solucion, visitadas):
    for fila in solucion:
        print(fila)
else:
    print("No hay un camino válido en el laberinto.")


"""

print("\n\nLABERINTO\n------------------")
lab = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]



def laberinto(f, c, lab):
    lab[f][c] = 2
    if f == len(lab) - 1 and c == len(lab[0]) - 1:
        print("He llegado")
        for fila in lab:
            print(fila)
    else:
        #Abajo
        if f < len(lab) - 1 and lab[f+1][c] == 0:
            laberinto(f+1,c,lab)

        #Derecha
        if c < len(lab[0]) - 1 and lab[f][c+1] == 0:
            laberinto(f,c+1,lab)

        #Izquierda
        if c > 0 and lab[f][c-1] == 0:
            laberinto(f,c-1,lab)

        #Arriba
        if f > 0 and lab[f-1][c] == 0:
            laberinto(f-1, c, lab)

    lab[f][c] = 0


laberinto(0,0,lab)