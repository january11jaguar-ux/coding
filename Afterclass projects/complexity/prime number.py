#create a code that finds prime numbers with two numbers/digits

a = int(input("Enter first number (must be smaller than end or else the code wont work): "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)

