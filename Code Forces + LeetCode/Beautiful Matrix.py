import numpy as np 

for i in range(5):
    L=[int(c) for c in input().split()]
    if 1 in L:
        r_pos=i+1
        c_pos=L.index(1)+1
        print(abs(3-r_pos) + abs(3-c_pos))
        break




