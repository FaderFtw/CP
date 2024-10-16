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
n, m, k = read_inputs(int, 3)
applicants = read_to_list(int)
applicants.sort()
appartments = read_to_list(int)
appartments.sort()
ans = 0
papr = papp = 0
while papp < n and papr < m:
    if abs(applicants[papp] - appartments[papr]) <= k:
        ans += 1
        papr += 1
        papp += 1
    elif applicants[papp] < appartments[papr]:
        papp += 1
    else:
        papr += 1
print(ans)