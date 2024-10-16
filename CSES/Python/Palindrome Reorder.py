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
s = input()
map ={}
for c in s:
    if c in map:
        map[c]+=1
    else:
        map[c] = 1
if len(map.keys()) == 1:
    print(s)
    exit()
odd = len(s) %2 != 0
found_odd = False
res=""
for c, count in map.items():
    if count % 2 != 0:
        if odd and not found_odd:
            found_odd = True
            mid = c * count
        else:
            print("NO SOLUTION")
            exit()
    else:
        res += c * (count // 2)
if odd:
    print(res + mid + res[::-1])
else:
    print(res + res[::-1])