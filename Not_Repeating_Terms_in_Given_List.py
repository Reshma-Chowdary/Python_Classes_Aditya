l = [int(x) for x in input('Enter a list of numbers: ').split()]
ml = []
for i in l:
    if(l.count(i) == 1):
        ml.append(i)
print(ml)
