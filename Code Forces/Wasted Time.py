n,k=map(int, input().split())
total=0
x1,y1=map(int,input().split())

for _ in range(n-1):
    x2,y2=map(int,input().split())
    total+=((x2-x1)**2+(y2-y1)**2)**(1/2)
    x1,y1=x2,y2

print((total/50)*k)

