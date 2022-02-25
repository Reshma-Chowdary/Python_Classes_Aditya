n = input()
l = []
'''for i in range(n):
    x = int(input())
    l.append(x)
'''
c = 0
e = []
x = input()
l = [int(i) for i in x.split()]
for i in l:
    if(i != 0):
        c += 1
        e.append(i)
print('The Number Of Non-Zero Elements In Given List Is --> ', c)
print('The Non-Zero Elements In Given List Are --> ', end="")
for i in e:
    print(i, end=" ")
