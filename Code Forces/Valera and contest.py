n,k,l,r,sall,sk=list(map(int,input().split()))

if r==l:
    print(' '.join([str(i) for i in [l]*n]))
else:    
    avg=sk//k
    scores=[avg]*k+[0]*(n-k)
    sall-=sk
    sk=sk%k

    i=0
    while(sk!=0):
        if sk > r-scores[i]:
            sk-=r-scores[i]
            scores[i]+=(r-scores[i])
        else:
            scores[i]+=sk
            sk=0
            break
        i+=1
    
    for i in range(k,n):
        scores[i]=l
    
    sall-=l*(n-k)

    i=k
    while(sall!=0):
        if sall > scores[k-1]-scores[i]:
            sall-=scores[k-1]-scores[i]
            scores[i]=scores[k-1]
        else:
            scores[i]+=sall
            sall=0
            break
        i+=1 

    print(' '.join([str(i) for i in scores]))

