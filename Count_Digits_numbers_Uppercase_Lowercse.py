d = a = uc = lc = 0
for i in input().split():
    for j in i:
        if j.isdigit():
            d += 1
        if j.isalpha():
            a += 1
        if j.isupper():
            uc += 1
        if j.islower():
            lc += 1
print(d)
print(a)
print(uc)
print(lc)
