import math
def gcd_two_numbers(x,y):
    if y == 0:
        return 
    return gcd_two_numbers(x,x%y)
    
def getGCD(nums):
    if len(nums) == 0: return -1
    gcd = nums[0]
    for i in range (1,len(nums)):
        gcd = gcd_two_numbers(gcd,nums[i])
    return gcd


clans = []
def dfs(l, progress, subset):
    if 1 in subset:
        return
    if(progress >= len(l)):
        if getGCD(subset) > 1 :
            clans.append(subset)
        return
    dfs(l, progress+1, subset+[l[progress]])
    dfs(l, progress+1, subset)
    

n = int(input())
army = list(map(int, input().split()))

dfs(army, 0, [])

power = 0
for clan in clans:
    power+=len(clan)*getGCD(clan)

print(power)