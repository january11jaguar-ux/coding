fname = input("Enter your name")
print("HELLO!! AND WELCOME",fname)
DOB = int(input("Enter the year you were born"))
current_year=2026
Age= current_year-DOB
print(fname," is",Age,"Years old")

print("What is 8+2... it is=", 8+2)

for I in range (5):
    print("m"*I)

number = int(input("Enter a number from 1-20: "))
odd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
even = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

if number in odd:
    print("This is an odd number")
elif number in even:
    print("This number is even")
else:
    print("Number is outside the 1-20 range")
