


lines=[]
for i in range(4):
    L=[c for c in input()]
    lines.append(L)

for i in range(3):
    state1=False
    for j in range(3):
        state=False
        if lines[i][j] == lines[i+1][j]:
                if lines[i][j+1] == lines[i+1][j+1] :
                    if lines[i][j] == lines[i][j+1]:
                        print("YES")
                        state=True
                        break
                else:
                    print("YES")
                    state=True
                    break
        else:
            if lines[i][j+1] == lines[i+1][j+1]:
                print("YES")
                state=True
                break
    if state:
        state1=True
        break
if not state1:
    print("NO")