def burbuja(vector):
    cambio=True
    iteración=0
    while (cambio == True):
        cambio = False
        iteración = iteración + 1
        for i in range(0, len(vector) - iteración):
            if (vector[i] > vector[i+1]):
                cambio = True
                aux=vector[i]
                vector[i]=vector[i+1]
                vector[i+1]=aux
    return vector
print(burbuja([2,9,8,5,6,3,2,1]))

def Qsort(vector):
    izq = []
    centro = []
    der = []
    if len(vector) > 1:
        pivote = vector[0]
        for i in vector:
            if i < pivote:
                izq.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                der.append(i)
        return Qsort(izq)+centro+Qsort(der)
    else:
      return vector
print(Qsort([2,9,8,5,6,3,2,1]))

def Mezcla(vector):
   # print("Dividir ",unaLista)
    if (len(vector)>1):
        mitad = len(vector)//2
        mitadIzquierda = vector[:mitad]
        mitadDerecha = vector[mitad:]
        Mezcla(mitadIzquierda)
        Mezcla(mitadDerecha)
        i=0
        j=0
        k=0
        while (i < len(mitadIzquierda) and j < len(mitadDerecha)):
            if (mitadIzquierda[i] < mitadDerecha[j]):
                vector[k]=mitadIzquierda[i]
                i=i+1
            else:
                vector[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while (i < len(mitadIzquierda)):
            vector[k]=mitadIzquierda[i]
            i=i+1
            k=k+1
        while (j < len(mitadDerecha)):
            vector[k]=mitadDerecha[j]
            j=j+1
            k=k+1
        return vector
print(Mezcla([9,8,6,5,2,2,3,1]))

