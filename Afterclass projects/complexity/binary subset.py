#create a binary subset and see how they add to the elements 
input("A set with n elements has 2^n subsets. Press Enter")

n = int(input("Enter number of elements: "))
guess= input("How many subsets does a set of "+str(n)+" elements have? ")
input("Each element is in or out - 2 choices per element. Press Enter")
print(" ",n," elements subsets: ", 2**n," your guess: ", guess)