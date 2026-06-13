#Hotel cost
def hotel_cost(nights):
    return 140*nights
#plane Ride cost
def Plane_ride_cost(city):
    if city == "charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "pittsburgh":
        return 222
    if city == "los Angeles":
        return 475
    
#Rantal car Cost
def Rantal_car_Cost(days):
    if days >= 7:
        return (40 * days) - 50
    elif days >= 3:
        return (40 * days) - 20
    else:
        return 40 * days
    
#Total trip cost
def trip_cost(city, days, spending_money):
    return (
        hotel_cost(days)
        + Plane_ride_cost(city)
        + Rantal_car_Cost(days)
        + spending_money
    )
#display results
print("Car rental costs : ",
      Rantal_car_Cost(5))
print("Plane costs : ",
      Plane_ride_cost("los Angeles"))
print("Hotel costs : ",
      hotel_cost(7))
print("Total trip costs : ",
      trip_cost("los Angeles",7,500))
print("Total Tampa trip Cost : ",
      trip_cost("Tampa",6,500))
