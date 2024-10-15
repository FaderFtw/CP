s=input()
if "bear" not in s:
    print(0)
else:
    res=0
    i=0
    while i < len(s)-4:
        j=4 
        while j < len(s):
            if 'bear' in s[i:j] :
                res+=1+len(s)-j
                i+=1
            else:
                j+=1
        
print(res)
