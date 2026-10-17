open_seats = [12, 15, 18, 25,26, 28,30, 31, 34]

print("The unoccupied seats on the train are ",str(open_seats))

max_waitong = input("Max checks to find any open seats in this list?")
s = int(input("Enter a seat number you hope you may get: "))

input("The system will now choose a seat for you. Press Enter to continue")
low, high = 0, len(open_seats) - 1
seats = 0
while low <= high:
    mid = (low + high) //2
    seats += 1
    print(" unoccupied seat: ", seats, " System considering: ", open_seats[mid])
 

input("The system has chosen a seat for you. Press Enter to see your assigned seat")
print("original choice",s,"system choice", seats)
