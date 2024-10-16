n = int(input())
numbers = map(int, input().split())
L = [i for i in range(1,n+1)]
print(list(set(L) - set(numbers))[0])