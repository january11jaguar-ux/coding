#using a try and except
try:
    number = int(input("Enter a number :"))
    print("The number enterred is : ",number)
#using Value error
except ValueError as ex:
    print("Exception: ",ex)
