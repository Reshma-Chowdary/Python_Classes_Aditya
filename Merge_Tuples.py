l1 = input('Enter student names: ').split()
l2 = input('Enter student roll numbers: ').split()
l3 = tuple(zip(l1, l2))
print(str(l3))
