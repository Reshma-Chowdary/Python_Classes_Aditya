temp=input()
s = [int(x) for x in input().split()]
t=[]
for x in s:
    if(x not in t):
        t.append(x)
t.sort
print(t[-2])
