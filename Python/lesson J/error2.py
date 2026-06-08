try:
    num1,num2=eval(input("Enter two numbers seperated by comma"))
    result = num1/num2
    print("Your result is : ",result)
#using several except for different errors

except ZeroDivisionError:
    print("XDivision by 0 is error!!!")
except SyntaxError:
    print("Comma not found. seperate the numbers with a comma like this : 4,5")
except :
    print("Wrong input")
else :
    print("No exceptions")
finally:
    print("This code will execute no matter what")