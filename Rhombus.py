n = int(input('Enter any odd number: '))
k = n//2
for i in range(1, n+1, 2):
    print(' '*k + '*'*i, end='')
    print()
    k -= 1
k = 1
for i in range(n-2, 0, -2):
    print(' '*k + '*'*i, end='')
    print()
    k += 1
