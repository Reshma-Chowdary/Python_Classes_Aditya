n = input()
x = input()
l = [int(i) for i in x.split()]
l.sort()
l.reverse()
for i in l:
    print(i, end=" ")
