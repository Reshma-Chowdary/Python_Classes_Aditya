n = int(input('Enter limit for list: '))
x = []
print('Enter', n, 'elements: ')
for i in range(1, n+1):
    p = int(input())
    x.append(p)
for i in range(0, n):
    x.sort()
print('Minimum number of given list --> ', x[0])
print('Maximum number of given list --> ', x[n-1])
