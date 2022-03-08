c = 0
n = input()
v = ['a', 'e', 'i', 'o', 'u']
for i in range(len(n)):
    if n[i] not in v:
        c += 1
print(c)
