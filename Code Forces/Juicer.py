n,b,d=[int(nb) for nb in input().split()]
oranges=[int(c) for c in input().split() if int(c) <= b]
aux=res=0
for i in oranges:
    aux+=i
    if aux > d :
        aux=0
        res+=1

print(res)

