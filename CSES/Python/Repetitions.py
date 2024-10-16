s = list(str(input()))
rep = 1
curr = 1
last = s.pop()
while len(s) > 0:
    ch = s.pop()
    if ch == last:
        curr += 1
        rep = max(curr, rep)
    else:
        rep = max(curr, rep)
        curr = 1
        last = ch
print(rep)