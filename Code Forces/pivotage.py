import fractions as fr 
import numpy as np 


print("les parametres de la matrice:")
nb_rows,nb_colomuns=(int(i) for i in input().split(' '))

#how to initialize a matrice with zeros with numpy
M=np.zeros((nb_rows,nb_colomuns))

for i in range(nb_rows):
    M[i]=input().split()

def Pivoter(M,r,s):        
    M[r]=(1/M[r,s])*M[r]
    for i in range(nb_rows):
        if i != r:
           M[i]=M[i]-M[i,s]*M[r]

    return M

while True:
    print("les parametres du pivotage:")
    r,s=(int(i) for i in input().split(' '))


    print(Pivoter(M,r,s))

    if (input('Do u wanna continue ? ').upper()== 'NO'):
        break
    
