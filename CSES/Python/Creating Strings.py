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
# Time limit: 1.00 s
# Memory limit: 512 MB
# Given a string, your task is to generate all different strings that can be created using its characters.
# Input
# The only input line has a string of length n. Each character is between a–z.
# Output
# First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.
# Constraints
# 1 \le n \le 8
# Example
# Input:
# aabac
# Output:
# 20
# aaabc
# aaacb
# aabac
# aabca
# aacab
# aacba
# abaac
# abaca
# abcaa
# acaab
# acaba
# acbaa
# baaac
# baaca
# bacaa
# bcaaa
# caaab
# caaba
# cabaa
# cbaaa
s = input()
n = len(s)
s = sorted(s)
ans = []
while True:
    ans.append(''.join(s))
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:
        break
    j = n - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = s[i + 1:][::-1]
print(len(ans))
for x in ans:
    print(x)