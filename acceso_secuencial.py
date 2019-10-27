#####################TIPOS DE FOR EN PYTHON#############################
#FOR CON CICLO WHILE
def acc_while(arr):
    i=0
    print("FOR CON WHILE")
    while(i<=(len(arr)-1)):
        print("El elemento del índice " + str(i)+ " es: "+ str(arr[i]))
        i=i+1

#FOR CON LISTAS
def forListas(arr):
    print("FOR CON LISTAS")
    for arreglo in arr:
        print ("Se accede a: {0}, su índice es: {1} ".format(
        arreglo, arr.index(arreglo)))

#FOR CON LISTAS Y LA FUNCIÓN RANGO
def forListAndRange(arr):
    print("FOR CON LISTAS Y FUNCIÓN RANGO")
    for i in range(len(arr)):
        print ("El índice "+str(i)+" tiene "+arr[i])

#FOR CON TUPLAS
def forInTuplas(arr):
    print("FOR CON TUPLAS")
    for i in arr:
        print ("El índice "+str(arr.index(i))+" es "+str(i))

#FOR EN DICCIONARIO
def forDiccionario(arr):
    print("FOR EN DICCIONARIO")
    clave = arr.keys()
    valor = arr.values()
    cantidad_datos = arr.items()
    for clave, valor in cantidad_datos:
        print (clave + ": " + valor)

#SE ACLARA QUE ÉSTOS SON LOS CICLOS PERMITIDOS EN LENGUAJE PYTHON
#NO EXISTE EL DO-WHILE NI EL FOREACH COMO SE HABIA SOLICITADO

x=['A','n','d','g','i','s','j','f']
y={'A':'a','n':'N','d':'D','g':'G','i':'I','s':'S','j':'J','f':'F'}
acc_while(x)
forListas(x)
forListAndRange(x)
forInTuplas(x)
forDiccionario(y)
