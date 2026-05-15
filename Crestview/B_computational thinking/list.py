vegetable = []
print(vegetable)
vegetable.append("Kales")
vegetable.append("Cabbage")
vegetable.append("cauliflower")
vegetable.append("lettuce")
vegetable.append("spinach")

print(vegetable)

vegetable[4]= "cucumber"

vegetable.append("Beetroot")
vegetable.append("carrot")

del vegetable[2]

print(vegetable)

numm = len(vegetable)

print(numm)

for i in range (numm):
    print(vegetable[i])

print("*-*"*20)

for i in range(numm):
    print(i+1,"-", vegetable[i])

if "carrot" in vegetable :
    print ("yes, carrot is in the list")
else:
    print("carrot is not in list")


