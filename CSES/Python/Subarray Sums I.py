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
n, target= read_inputs(int, 2)
numbers = read_to_list(int)
ans = 0
sum = 0
mp ={}
mp[0] = 1
for i in range(n):
    sum += numbers[i]
    if sum - target in mp:
        ans += mp[sum - target]
    if sum in mp:
        mp[sum] +=1
    else:
        mp[sum] = 1
print(ans)