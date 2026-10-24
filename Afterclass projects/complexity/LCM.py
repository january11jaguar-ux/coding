numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
multiply = numberLargest * numberSmallest

while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is", numberLargest)
lcm = multiply // numberLargest 
print("LCM is", lcm)