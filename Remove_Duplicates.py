n = [i for i in input()]
t = []
for i in n:
    if i not in t:
        t.append(i)
for i in t:
    print(i, end='')
