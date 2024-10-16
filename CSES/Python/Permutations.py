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
n = int(input())
if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    res = []
    for i in range(2, n+1, 2):
        res.append(i)
    for i in range(1, n+1, 2):
        res.append(i)
    print_list(res)