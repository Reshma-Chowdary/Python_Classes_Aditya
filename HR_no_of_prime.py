n = int(input())
for i in range(n):
    l, u = [int(x) for x in input().split()]
    count = 0
    for i in range(l+1, u):
        k = 0
        for j in range(1, i+1):
            if(i % j == 0):
                k += 1
        if(k == 2):
            count += 1
    print(count)
