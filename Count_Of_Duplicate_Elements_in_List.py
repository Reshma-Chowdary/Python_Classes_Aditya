print('Enter elements into list: ')
l = input().split()
m = []
c = 0
for i in l:
    if l.count(i) > 1:
        c += 1
        l.remove(i)
print('Repeated elements: ', c)
