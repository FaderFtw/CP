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
q= int(input())
for _ in range(q):
    k = int(input())
    start, end, digitsLength, digitsToAdd = 1, 9, 1, 9 #10, 99, 2, 180
    while k > digitsToAdd:
        k -= digitsToAdd
        start *= 10
        end = end * 10 + 9
        digitsLength += 1 
        digitsToAdd = (end - start + 1) * digitsLength
    target = start + (k - 1) // digitsLength
    print(str(target)[(k - 1) % digitsLength])