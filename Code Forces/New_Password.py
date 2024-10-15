import random

n,k=[int(c) for c in input().split()]
ch="abcdefghijklmnopqrstuvwxyz"
ref=[c for c in ch]

ref1=[]
i=0
while i < k:
    c=ref[random.randint(0,len(ref)-1)]
    if c not in ref1:
        ref1.append(c)
        i+=1

word=ref1[:]

i=k
while i < n:
    c=ref1[random.randint(0,k-1)]
    if c != word[i-1]:
        word.append(c)
        i+=1

print(''.join(word))