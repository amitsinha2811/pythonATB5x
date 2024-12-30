# Quardratic Equation = ax**2 + bx + c =0
# a,b and c are real
#a!=0

import cmath

a= int(input("Enet the number(a!=0) :"))
b= int(input("Enet the number :"))
c= int(input("Enet the number :"))

d= (b**2)-(4*a*c)

root1 = (-b + cmath.sqrt(d))/(2*a)
root2 = (-b - cmath.sqrt(d))/(2*a)

print("The roots are :",root1, "and", root2)