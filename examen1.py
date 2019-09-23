def arr(arreglo):
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
print(arr(x))