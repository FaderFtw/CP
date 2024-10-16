def read_to_list(arg_type):
    return list(map(arg_type, input().strip().split()))
def read_inputs(arg_type, n):
    if n == 1:
        return arg_type(input().strip())
    else:
        return list(map(arg_type, input().strip().split()))
def read_pairs(arg_type, n):
    pairs = []
    for idx in range(n):
        pairs.append(read_inputs(arg_type, 2) + [idx + 1])
    return pairs
def print_list(list):
    res =""
    for element in list:
        res+= str(element) + ' '
    print (res[:len(res)-1])
def construct_matrix(n, m):
    matrix = []
    for j in range(n):
        s = [x for x in str(input())]
        matrix.append(s)
    return matrix
n, x = read_inputs(int, 2)
children = read_to_list(int)
children.sort(reverse=True)
ans = 0
i = 0 
while i < n :
    if children[i] >= x:
        i+=1
    elif children[i] + children[len(children)-1] <= x:
        i+=1
        children.pop()
        n-=1
    elif i != n-1 and children[i] + children[i+1] <= x:
        i+=2
    else:
        i+=1     
    ans+=1
print(ans)