#Funcion que regrese el producto de multiplicar sus elementos, arreglo NO VACÍO
def multiplicar(arr):
    mult=1
    for i in range (len(arr)):
        mult=mult*arr[i]
    return mult

x=[1,2,3,4,5,6,7,8,9] 
print(multiplicar(x)) #362880
y=[1,2,3,4] 
print(multiplicar(y)) #24