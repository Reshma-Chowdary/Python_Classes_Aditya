p1 = 500
p2 = 300
p3 = 2000
p4 = 1000
p5 = 500
print('Prices Of Products Available : ')
print("\tHoney -> 500/- only")
print("\tface wash -> 300/-")
print("\tPerfume -> 2000/- only")
print("\tBowl Set -> 1000/- only")
print("\tcashew-1/2kg -> 500/- only")
print()
c1 = int(input('Enter no of honey bottles: '))
c2 = int(input('Enter no of face washes : '))
c3 = int(input('Enter no of perfumes : '))
c4 = int(input('Enter no of bowl sets : '))
c5 = int(input('Enter no of cashew packets : '))
total = (p1*c1)+(p2*c2)+(p3*c3)+(p4*c4)+(p5*c5)
if(total > 5000):
    dis = total*10/100
    tax = total*10/100
elif(total > 3000):
    dis = total*8/100
    tax = total*10/100
elif(total > 2000):
    dis = total*5/100
    tax = total*18/100
elif(total > 1000):
    dis = total*3/100
    tax = total*18/100
bill = total-dis+tax
print("Bill = ", bill)
