# 1s -> 10^8 operations
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
# i have to read integers on the same line but i want to read them one by one 
n= int(input())
coins = read_to_list(int)
coins.sort()
if coins[0] != 1 :
    print(1)
else:
    ans = 0
    for coin in coins:
        if coin > ans + 1:
            print(ans + 1)
            exit()
        ans += coin
    print(ans + 1)