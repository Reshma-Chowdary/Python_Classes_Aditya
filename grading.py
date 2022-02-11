sno = int(input("Enter Student no : "))
sname = input('Enter Student Name : ')
sgroup = input('Enter Student Group : ')
print('Enter the following subject marks you scored : ')
s1 = int(input('Enter Telugu Marks : '))
s2 = int(input('Enter English Marks : '))
s3 = int(input('Enter Maths Marks : '))
s4 = int(input('Enter stat Marks : '))
s5 = int(input('Enter DBMS Marks : '))
s6 = int(input('Enter Python Marks : '))
avg = (s1+s2+s3+s4+s5+s6)/6
print('Average : ', avg)
if(avg > 91):
    print('You secured O Grade')
elif(avg > 81):
    print('You secured A Grade')
elif(avg > 71):
    print('You secured B Grade')
elif(avg > 61):
    print('You secured C Grade')
elif(avg > 51):
    print('You secured D Grade')
elif(avg > 41):
    print('You secured E Grade')
else:
    print("You are fail")
