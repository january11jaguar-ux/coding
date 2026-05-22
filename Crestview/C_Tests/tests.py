trees=["Oak","Beech","Willow"]
print(trees)
num_tree=len(trees)
print(num_tree)

i = input("Enter an index number from 0-2 : ")
i = int(i)

if i<len(trees):
    print(trees[i])
else:
    print("out of bounds Error")

ice_cream = []

print("*-*-*-*"*15)
print("This is just a side quest")

for i in range (6):
    flavour = input("enter an ice cream flavour")
    ice_cream.append(flavour)

print(ice_cream)
