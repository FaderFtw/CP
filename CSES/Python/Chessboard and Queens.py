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
        ref = {'.': False, '*': True}
        s = [ref[x] for x in str(input())]
        matrix.append(s)
    return matrix
reserved = construct_matrix(8,8)
col = [ False for _ in range(16)]
diag1 = [ False for _ in range(16)]
diag2 = [ False for _ in range(16)]
ways = 0
def search(r):
    global ways
    if (r == 8):
        ways +=1
        return
    for c in range(8):
        if(col[c] or diag1[r+c] or diag2[r-c+7] or reserved[r][c]):
            continue
        col[c] = diag1[r+c] = diag2[r-c+7] = True
        search(r+1)
        col[c] = diag1[r+c] = diag2[r-c+7] = False
search(0)
print(ways)