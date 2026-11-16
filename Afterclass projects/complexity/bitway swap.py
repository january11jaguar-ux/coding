#do not swap with another variable detect if positive or negative left shift 

n = int(input("Enter a number (try 3 or 7):"))
guess = input("After XOR swap of "+str(n)+" and 8 what does n become? ")
a, b = n, 8
a ^= b; b^= a; a^= b
input("XOR swap exchanges the values. Press Enter")
print("n became: ",a," your guess: ", guess)

guess = input("What is "+str(n)+" <<2")
input("Left shift by 2 multiplies by 4. Press Enter ")
print(" ", n, " <<2= ", n << 2," your guess: ", guess)

guess = input('Will '+str(n)+" ^-8 be positive or negative? ")
input("XOR is negative when signs differ. Press Enter ")
print(" ",n,"^-8= ", n ^ -8, " your guess: ", guess)