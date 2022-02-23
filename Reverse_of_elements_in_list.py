n = int(input('Enter limit for list: '))
x = []
print('Enter', n, 'elements: ')
for i in range(1, n+1):
    x.append(int(input()))
print('Before sorting: ', x)
x.reverse()
print('After sorting: ', x)
