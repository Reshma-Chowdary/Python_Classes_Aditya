n = int(input())
t = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if(i % j == 0):
            sum = sum+1
    if(sum == 2):
        t = t+i
print(t)
