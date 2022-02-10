Roll_no = int(input('Enter student no:'))
Name = input('Enter student name:')
Group = input('Enter student group')
s1 = int(input('Telugu :'))
s2 = int(input('English :'))
s3 = int(input('Maths :'))
s4 = int(input('stat :'))
s5 = int(input('DBMS :'))
s6 = int(input('Python :'))
if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35 and s6 >= 35:
    print('Pass')
else:
    print('Fail')
