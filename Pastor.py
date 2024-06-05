def pastorcito(p,l,o,c,estados, camino):
    estados.append([p,l,o,c])
    camino.append([p, l, o, c])
    if p=="I" and l=="I" and o=="I" and c=="I":
        for c in camino:
            print(c)
    else:
        #Mover Lobo:
        if p=="D":
            if l=="D" and (o=="I" or c=="I") and ["I", "I", o, c] not in estados:
                pastorcito("I", "I", o, c, estados, camino)
                camino.pop()
        else:
            if l=="I" and (o=="D" or c=="D") and ["D", "D", o, c] not in estados:
                pastorcito("D", "D", o, c, estados, camino)
                camino.pop()
        #Mover oveja:
        if p=="D":
            if o=="D" and["I", l, "I", c] not in estados:
                pastorcito("I", l, "I", c, estados, camino)
                camino.pop()
        else:
            if o=="I" and["D", l, "D", c] not in estados:
                pastorcito("D", l, "D", c, estados, camino)
                camino.pop()
        # Mover Lobo:
        if p == "D":
            if c == "D" and (o == "I" or l == "I") and ["I", l, o, "I"] not in estados:
                pastorcito("I", l, o, "I", estados, camino)
                camino.pop()
        else:
            if c == "I" and (o == "D" or l == "D") and ["D", l, o, "D"] not in estados:
                pastorcito("D", l, o, "D", estados, camino)
                camino.pop()
        #Mover pastor:
        if p=="D":
            if (l=="D" and o=="D") == False and (o=="D" and c=="D") == False and ["I", l, o, c] not in estados:
                pastorcito("I", l, o, c, estados, camino)
                camino.pop()
        else:
            if (l=="I" and o=="I") == False and (o=="I" and c=="I") == False and ["D", l, o, c] not in estados:
                pastorcito("D", l, o, c, estados, camino)
                camino.pop()



pastorcito("D","D","D","D",[],[])