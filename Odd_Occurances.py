l = [int(x) for x in input('Enter a list of values : ').split()]
ml = []
for j in l:
    if(l.count(j) % 2 != 0):
        ml.append(j)
        l.remove(j)
print(ml)
