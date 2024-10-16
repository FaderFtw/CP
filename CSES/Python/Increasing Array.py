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
def pl(s):
    print(s, end=" ")
def construct_matrix(n, m):
    matrix = []
    for j in range(n):
        s = [x for x in str(input())]
        matrix.append(s)
    return matrix
n = int(input())
numbers = read_to_list(int)
res = 0
for i in range(1,n):
    if(numbers[i] < numbers[i-1]):
        res += numbers[i-1] - numbers[i]
        numbers[i] = numbers[i-1]
print(res)