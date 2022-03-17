print('Enter PassWord:(Password should contain 1 upper,1 lower,1 symbol and 1 digit):  ')
l = [i for i in input()]
uc = 0
lc = 0
sc = 0
dc = 0
for i in l:
    if i.isupper():
        uc += 1
    elif i.islower():
        lc += 1
    elif i.isnumeric():
        dc += 1
    else:
        sc += 1
if(uc == 0 or lc == 0 or sc == 0 or dc == 0):
    print('Your password is INVALID')
    print('Your Password should contain 1 upper,1 lower,1 symbol and 1 digit....')
else:
    print('Your password is VALID')
