v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
l = []
for i in input('Enter a string: '):
    l.append(i)
for i in l:
    if i in v:
        l.remove(i)
print('Resultant String: ')
for i in l:
    print(i, end='')
