#Check if bit is ON or OFF
n = int(input("Enter a number (try 42 or 13)"))
guess = input(" Is bit 2 of " + str(n)+" (ON/OFF)?")
input("Check if the Nth bit is set - AND with the mask. Press Enter")
result = (n >> 2) & 1
if result :
    print(" ",n," binary: ", bin(n)[2:]," bit 2 is ON your guess: ", guess)
else: 
     print(" ",n," binary: ", bin(n)[2:]," bit 2 is OFF your guess: ", guess)