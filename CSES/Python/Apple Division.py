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
def AppleDivision(i, n, sum1, sum2, numbers, res):
    if i == n:
        res = min(res, abs(sum1 - sum2))
    else:
        res = AppleDivision(i + 1, n, sum1 + numbers[i], sum2, numbers, res)
        res = AppleDivision(i + 1, n, sum1, sum2 + numbers[i], numbers, res)
    return res
n = int(input().strip())
numbers = read_to_list(int)
res = 10**18
res = AppleDivision(0, n, 0, 0, numbers, res)
print(res)