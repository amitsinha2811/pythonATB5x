'''n = int(input("Enter the Number(0 to 100) :"))
if n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Wierd")'''
import math
import os
import random
import re
import sys

n = int(input())
if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")