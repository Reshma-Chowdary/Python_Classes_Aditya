print('Enter Scores : ')
l = input().split()
m = []
for i in l:
    if i not in m:
        m.append(i)
m.sort()
print('Second Runner Up Score: ', m[-3])
