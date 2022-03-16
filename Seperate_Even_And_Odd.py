l = [int(i) for i in input('Enter list: ')]
e = []
o = []
for i in l:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
print('The even list is ', end='')
for i in e:
    print(i, end='')
print()
print('The odd list is ', end='')
for i in o:
    print(i, end='')
