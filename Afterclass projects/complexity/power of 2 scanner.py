#Create a power of 2 scanner that can check power of 4, and 8 too

n = int(input("Enter a number: "))
guess = input("Is "+ str(n)+" a power of 2? (yes/no)")
input("Power of 2: n & (n-1) == 0 means only one bit is ON. press enter")
if n > 0 and (n &(n-1)) == 0:
    print(" ",n," binary:  ", bin(n)[2:], " power of 2: yes your guess: ", guess)
else:
    print(" ",n," binary:  ", bin(n)[2:], " power of 2: no your guess: ", guess)


n = int(input("Enter a number: "))
guess = input("Is "+str(n)+" a power of 4? (yes/no): ")
input("check: n % 3 == 1. Press Enter ")
is_pow4 = n > 0 and (n&(n-1)) == 0 and n%3 == 1
if is_pow4:
    print(" ", n, " binary: ", bin(n)[2:]," power of 4: yes your guess", guess)
else:
    print(" ", n, " binary: ", bin(n)[2:]," power of 4: no your guess", guess)