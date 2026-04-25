units = int(input("Please enter the amount of units you consumed: "))

if (units < 50) :
    amount = units*2.60
    surcharge=25

elif (units <=100):
    amount=130+((units-50)*3.25)
    surcharge= 35

elif (units<=200):
    amount=130+162.50((units-100)*5.26)
    surcharge=45

else:
    amount= 130+162.50