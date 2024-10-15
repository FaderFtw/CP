n=int(input())
L=list(map(int,input().split()))
L.sort()
for i in range(n-2):
    state = False
    if L[i]+L[i+1] > L[i+2]:
        print("YES")
        state = True
        break

if not state:
    print("NO")
        

