#Compare three different ways to work with the quiz course
n = 15

guesss = input(" Which is the best(most used) division method for 115 divided by 20: 1.\n 1. Long divison \n 2. Short division. \n Pick 1 or 2 (Press Enter to run) ")

input(" Short division: Press Enter to run")
uses = 5
print("  uses:", uses, "  The is a smaller way to divide and is best for small divisons.")

input("  Long division: Press Enter to run")
uses = 0
for i in range (n):
    for j in range (n):
        uses +=1
print("  uses:", uses, " Long divison is best for large numbers and also can be use with small numbers it is the most accurate")

print(" n=", n)
