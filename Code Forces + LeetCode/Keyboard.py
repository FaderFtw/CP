ref="qwertyuiop asdfghjkl; zxcvbnm,./"


if input() == 'R':
    key=-1
else:
    key=1
msg=input()
res=''
for c in msg:
    res+=ref[ref.index(c)+key]

print(res)
