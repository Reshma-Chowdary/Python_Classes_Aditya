n = int(input())
for l in range(n):
    l = int(input())
    count = 0
    for i in range(1, l+1):
        k = 0
        for j in range(1, i+1):
            if(i % j == 0):
                k += 1
        if(k == 2):
            count += 1
    print(count)
