import random
def busq_lineal(vector, elemento):
    for j in range (10000):
        vector.append(random.randint(0, 100))
    i=0
    for i in range (len(vector)):
        if(vector[i]==elemento):
            return i 
        else: 
            i=i+1
        #print(vector)
    return -1

print(busq_lineal([],7))
print(busq_lineal([],99))
print(busq_lineal([],101))
print(busq_lineal([],44))