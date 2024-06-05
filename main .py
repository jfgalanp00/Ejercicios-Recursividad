#Para que sea recursivo necesitamos:
#caso de parada
#caso de llamada a la funcion cambiando alguno de los parametros
# def sumalista(1)
#   if(2)
#       ********
#   else:
#       sumalista(3)

#1. Suma de elementos en una lista: Escribe una función recursiva para calcular la suma de todos los elementos en una lista.
def suma_lista(indice, lista):
    if indice == len(lista):
        return 0
    else:
        return lista[indice] + suma_lista(indice+1, lista)

lista = [4, 2, 2, 4, 2]
i = 0

print(lista)
print(suma_lista(i, lista))

def sum(lista, index, suma):
    if index == len(lista):
        print(suma)
    else:
        suma += lista[index]
        sum(lista, index+1, suma)

lista = [4, 2, 2, 4, 2]
sum(lista, 0, 0)

# 2. Factorial de un número: Escribe una función recursiva para calcular el factorial de un número entero utilizando una lista de números.
def factorial(n, lista):
    if n == 0:
        return 1
    else:
        return lista[n-1] * factorial(n-1, lista)

numeros = [5, 4, 3, 2, 1]
print(factorial(len(numeros), numeros))
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)

entero = 5
print(factorial2(entero))

# 3. Fibonacci: Escribe una función recursiva para generar los primeros n términos de la secuencia de Fibonacci utilizando una lista.
# 0 1 1 2 3 5 8 13 21

def fibonacci(n1, n2, entero):
    if n1 == entero:
        return print("fin")
    else:
        suma = n1 + n2
        print(suma)
        return fibonacci(n2, suma, entero)

entero = 0
n1 = 0
n2 = 1

fibonacci(n1, n2, entero)

# 4 Buscar un elemento en una lista: Escribe una función recursiva para buscar un elemento específico en una lista.
def buscar_elemento(lista, elemento):
    if len(lista) == 0:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return buscar_elemento(lista[1:], elemento)

mi_lista = [1, 2, 3, 4, 5]
mi_elemento = int(input("introduce un numero para comprobar si esta en la lista "))
resultado = buscar_elemento(mi_lista, mi_elemento)

if resultado == True:
    print("El elemento de la lista "+ mi_elemento.__str__() + " Se encuentra en la lista ")
else:
    print("El elemento de la lista " + mi_elemento.__str__() + " No se encuentra en la lista ")


# 5. Invertir una lista: Escribe una función recursiva para invertir una lista dada
def invertir_lista(lista):
    if len(lista) == 0:
        return [0]
    else:
        return [lista[-1]] + invertir_lista(lista[:-1])
lista = [1, 2, 3, 4, 5]
#lista = [5, 4, 3, 2, 1]
lista_invertida = invertir_lista(lista)
print(lista_invertida)

#6. Eliminar elementos duplicados: Escribe una función recursiva para eliminar elementos duplicados de una lista.
def eliminar_duplicados(lista, indice):
    if indice == len(lista):
        return lista
    else:
        valor = lista[indice]
        while lista.count(valor) > 1:
            lista.remove(valor)
        return eliminar_duplicados(lista, indice + 1)

lista = [1, 0, 0, 3, 4, 4, 5, 6, 6, 7]
print(lista)
eliminar_duplicados(lista, 0)
print(lista)

#7. Ordenar una lista: Escribe una función recursiva para ordenar una lista de números utilizando un algoritmo de ordenación recursiva, como Merge Sort o Quick Sort.
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    izquierda, medio, derecha = [], [], []

    for x in lista:
        if x < pivote:
            izquierda.append(x)
        elif x == pivote:
            medio.append(x)
        else:
            derecha.append(x)

    return quicksort(izquierda) + medio + quicksort(derecha)

mi_lista = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(mi_lista))

#8. Calcular la potencia de un número: Escribe una función recursiva para calcular la potencia de un número utilizando una lista.
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * potencia_recursiva(base, exponente - 1)
    else:
        return 1 / (base * potencia_recursiva(base, -exponente - 1))

base = 2
exponente = 3
resultado = potencia_recursiva(base, exponente)
print(f'{base}^{exponente} = {resultado}')

#9. Comprobar si una lista es palíndromo: Escribe una función recursiva para verificar si una lista es un palíndromo, es decir, se lee igual de adelante hacia atrás.
def es_palindromo(lista, inicio, fin):
    if inicio >= fin:
        return True
    else:
        if lista[inicio] == lista[fin]:
            return es_palindromo(lista, inicio + 1, fin - 1)
        else:
            return False

lista1 = [1, 2, 3, 2, 1]
lista2 = [1, 2, 3, 4, 5]

if es_palindromo(lista1, 0, len(lista1) - 1):
    print("La lista 1 es un palíndromo.")
else:
    print("La lista 1 no es un palíndromo.")

if es_palindromo(lista2, 0, len(lista2) - 1):
    print("La lista 2 es un palíndromo.")
else:
    print("La lista 2 no es un palíndromo.")


from pip._internal.commands.show import print_results

#10. Generar todas las combinaciones de una lista: Escribe una función recursiva para generar todas las posibles combinaciones de una lista de elementos.
# la salida por pantalla tiene que ser la siguiente:
#[]
#[1]
#[1,2]
#[2,3]
#[1,3]
#[1,2,3]
def generar_combinaciones(lista, r):
    if r == 0:
        return [[]]
    elif len(lista) < r:
        return []
    else:
        primera_combinacion = [[lista[0]] + resto for resto in generar_combinaciones(lista[1:], r - 1)]
        segunda_combinacion = generar_combinaciones(lista[1:], r)
        return primera_combinacion + segunda_combinacion

mi_lista = [1, 2, 3, 4]
tamanio_combinacion = 2
combinaciones = generar_combinaciones(mi_lista, tamanio_combinacion)

for combinacion in combinaciones:
    print(combinacion)

def combi(l):
    if not l:
        return [[]]
    primer_elemento = l[0]
    resto = l[1:]

    combinacionnesResto = combi(resto)

    nuevasConvinaciones = []
    for combinacion in combinacionnesResto:
        nuevasConvinaciones.append(combinacion)
        nuevasConvinaciones.append([primer_elemento]+combinacion)

    return nuevasConvinaciones

l = [1, 2, 3]
combinaciones = combi(l)
for combinacion in combinaciones:
    print(combinacion)
    
def combinaciones(lista):
    if len(lista) == 0:
        return [[]]
    else:
        combinaciones = []
        primer_elemento = lista[0]
        combinaciones_restantes = combinaciones(lista[1:])
        for combinacion in combinaciones_restantes:
            combinaciones.append(combinacion)
            combinaciones.append([primer_elemento] + combinacion)
        return combinaciones

mi_lista = [1, 2, 3]
combinaciones = combinaciones(mi_lista)

for combinacion in combinaciones:
    print(combinacion)
