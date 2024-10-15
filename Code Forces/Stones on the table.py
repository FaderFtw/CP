n=int(input())
stones=input()
res=0
i=1
while i<n:
    if stones[i] == stones[i-1]:
        res+=1
    i+=1
print(res)
