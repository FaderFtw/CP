n,m,k=map(int,input().split())

L=[[0 for i in range(m)]for j in range(n)]

for i in range(k):
    a,b,val=map(int,input().split())
    if(a == 1):
        L[b-1] = [val for i in range(m)]
    else:
        for i in range(n):
            L[i][b-1] = val

def transform_str(L):
    s=str(L[0])
    for i in range(1,len(L)):
        s=s+' '+str(L[i])
    return s

for i in range(n):
    print(transform_str(L[i]))
    
        









#ref[(a,b,i)]=val

#ref=sorted(ref.items(), key=lambda item: item[0][2])