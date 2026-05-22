colorlist=["Red","Yellow","Blue","Green"]
final_value=len(colorlist)-1
print("Index numbers allowed go from 0 to",final_value)

user_choice = input("nter a number to display one color in the list :")
user_choice=int(user_choice)

if user_choice<len(colorlist) and user_choice>=0:
    print(colorlist[user_choice])
else:
    print("Your entry is invalid. Try a number between 0-3 dont be a bozo you only gotta choose four numbers it isnt that hard")
