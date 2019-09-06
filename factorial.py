def factorial(n):
    res=1
    conta=1
    if(n==0 or n==1):
        return 1
    if(n>1 and n<=10):
        for conta in range (1,n):
            res=n*(factorial(n-1))
    return res

def conseguirDatos(n):
    fac=1
    if(n>=0 and n<=10):
        fac=factorial(n)
    else:
        print("error")
    return fac

n=int(input(("Dame el número: ")))
x=conseguirDatos(n)
print("El factorial de ",n,"es ",x)