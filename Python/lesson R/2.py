#create class 
class Parrot :
    #create atributte
    species = "birds"
    #insistant atribute
    def __int__(self, name, age):
        self.name = name 
        self.age = age

#insistantiate the parrot class
blu = Parrot ("blu", 10)
Woo = Parrot ("Woo", 15)

#Access the class atribute
print("blu is a {}".format(blu.species))
print("Woo is a {}".format(Woo.species))

#access the instance atribute
print("{} is {} years old".format(blu.name , blu.age))
print("{} is {} years old".format(Woo.name , Woo.age))