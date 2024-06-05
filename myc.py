def mc(md, cd, mi, ci, b, estados):
    estados.append([md,cd,mi,ci,b])
    if mi == 3 and ci == 3:
        print("SOLUCION ENCONTRADA")
    else:
        #mover 2 canibales
        if b == True:
            if cd >= 2 and (ci+2 <= mi or mi==0) and [md, cd-2, mi, ci+2, False] not in estados:
                mc(md, cd-2, mi, ci+2, False, estados)
        else:
            if ci >= 2 and (cd+2 <= md or md==0) and [md, cd+2, mi, ci-2, True] not in estados:
                mc(md, cd+2, mi, ci-2, True, estados)

        # mover 2 misioneros
        if b == True:
            if md >= 2 and (md-2>=cd or md-2==0) and [md-2, cd, mi+2, ci, False] not in estados:
                mc(md-2, cd, mi+2, ci, False, estados)
        else:
            if mi >= 2 and (mi-2>=ci or mi-2==0) and [md+2, cd, mi-2, ci, True] not in estados:
                mc(md+2, cd, mi-2, ci, True, estados)

        # mover 1 misionero y 1 canibal
        if b == True:
            if md>=1 and cd>=1 and cd==md and [md-1, cd-1, mi+1, ci+1, False] not in estados:
                mc(md-1, cd-1, mi+1, ci+1, False, estados)
        else:
            if mi >= 1 and ci>=1 and cd==md and [md+1, cd+1, mi-1, ci-1, True] not in estados:
                mc(md+1, cd+1, mi-1, ci-1, True, estados)

        # mover 1 misionero
        if b == True:
            if md>=1 and md>cd and [md-1, cd, mi+1, ci, False] not in estados:
                mc(md-1, cd, mi+1, ci, False, estados)
        else:
            if mi>=1 and mi>ci and [md+1, cd, mi-1, ci, True] not in estados:
                mc(md+1, cd, mi-1, ci, True, estados)

        # mover 1 canibal
        if b == True:
            if cd>=1 and (ci+1<=mi or mi==0) and [md, cd-1, mi, ci+1, False] not in estados:
                mc(md, cd-1, mi, ci+1, False, estados)
        else:
            if ci>=1 and (cd+1<=md or md==0) and [md, cd+1, mi, ci-1, True] not in estados:
                mc(md, cd+1, mi, ci-1, True, estados)



#Barca True si derecha
mc(3,3,0,0,True,[])