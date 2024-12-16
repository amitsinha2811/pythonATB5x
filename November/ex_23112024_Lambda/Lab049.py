def find_even_odd(num):
    if num % 2==0:
        print("Even")
    else:
        print("Odd")

find_even_odd(5)
find_even_odd(16)

check_even_odd = lambda num: "Even" if num % 2==0 else "Odd"
print(check_even_odd(19))
print(check_even_odd(20))