n = int(input('Enter a number : '))
sum = 0
rem = 0
while n > 0:
    rem = n % 10
    sum = sum+rem
    n = n//10
print('The sum of individual digits of a given number is ', sum)
