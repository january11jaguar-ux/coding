#create class 
class Dog :
    #create atributte
    species = "Dog breed"
    #insistant atribute
    def __init__(self, name, age):
        self.name = name 
        self.age = age

#insistantiate the parrot class
German_Shepherd = Dog ("German Shepherd", 7)
Chihauhau = Dog ("Chihauhau", 5)

#Access the class atribute
print("German Shepherd is a {}".format(German_Shepherd.species))
print("Chihauhau is a {}".format(Chihauhau.species))

#access the instance atribute
print("{} is {} years old".format(German_Shepherd.name , German_Shepherd.age))
print("{} is {} years old".format(Chihauhau.name , Chihauhau.age))