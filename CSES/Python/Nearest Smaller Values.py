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
        pairs.append(tuple(read_inputs(arg_type, 2), idx))
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
# 1s -> 10^8 operations
n = int(input())
numbers = read_to_list(int)
nl = []
for i,number in enumerate(numbers):
    nl.append(i - 1)
    while nl[i] != -1 and numbers[nl[i]] >= number:
        nl[i] = nl[nl[i]]
    print(nl[i] + 1, end = ' ')