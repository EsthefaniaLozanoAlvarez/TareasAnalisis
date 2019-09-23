def arrExam(arreglo):
    arrnew=[]
    for j in range (0,len(arreglo)):
        aux=False
        for k in range (j,len(arreglo)):
            if(k!=j):
                if(arreglo[j]==arreglo[k]):
                    aux=True
        if(aux==False):
            arrnew.append(arreglo[j])
        for i in range (0,len(arrnew)):
            if(arrnew[i]==arreglo[i]):
                arrnew.remove(arrnew[i])
        for i in range (0,len(arrnew)):
            if(arrnew[i]==arreglo[k]):
                arrnew.remove(arrnew[i])
    return arrnew

x=[9,3,1,3,2,9]
print(arrExam(x))

#CÓDIGO CORREGIDO
lista_nueva = []
lista_original=[9,3,1,3,2,9]
conta=0
for j in range (len(lista_original)):
    conta=0
    for i in range (0,len(lista_original)):
        if( lista_original[j]==lista_original[i]):
            conta=conta+1 
    if(conta==1):   
        lista_nueva.append(lista_original[j])
print(lista_nueva)