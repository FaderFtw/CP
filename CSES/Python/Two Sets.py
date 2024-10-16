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
res = set()
if ((n*(n+1)) % 4 != 0):
    print("NO")
else:
    print("YES")
    sum = (n*(n+1))//4
    curr_sum = 0
    px = 1
    if sum % n == 0 :
        res.add(n)
        curr_sum += n
    while (curr_sum != sum):
        if(sum % n == 0):
            res.add(n-px)
            res.add(px)
            curr_sum += n
        else:
            res.add(n-px +1)
            res.add(px)
            curr_sum += n + 1
        px += 1
    a = len(res)
    print(a)
    out1 = out2 = ""
    for i in range(1,n+1):
        if i in res:
            out1 += str(i) + ' '
        else:
            out2 += str(i) + ' '
    print(out1[:len(out1) - 1])
    print(n - a)
    print(out2[:len(out2) - 1])