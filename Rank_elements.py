l = [int(x) for x in input().split()]
print([sorted(l).index(x)+1 for x in l])
