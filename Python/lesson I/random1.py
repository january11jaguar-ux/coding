import random
play = True
number = str(random.randint(0,9))

print ("I will choose a number from 0-9 and you have to guess each one at a time")
print ("The game ends when you get one hero")

while play:
    guess = input("give me your best guess : \n")
    if number == guess :
        print("you win the game")
        print("the number was : ",number)
        break

    else :
        print("Your guess isnt quiet right.try again\n")