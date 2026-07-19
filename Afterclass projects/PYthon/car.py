class  BM():
    def mileage(self):
        print("The mileage of BMW is : 217")

    def max_speed(self):
        print("The max speed of a BMW is : 300 km/h.")
    def type(self):
        print("BMW offers a range of models, including sedans, coupes, and electric vehicles, with various engine types such as inline-six, V6, V8, and hybrid options. For specific models like the BMW 320i, detailed performance metrics such as acceleration and top speed can be found in dedicated ")

class  Ferari():
    def mileage(self):
        print("The mileage of a Ferari is : 217")
    def max_speed(self):
        print("The max speed of a Ferari is : 355 km/h")
    def type(self):
        print("A Ferari is r fuel efficiency, with some models offering hybrid options for better fuel economy.These specifications highlight the performance capabilities of Ferrari vehicles, making them a favorite among car enthusiasts.Sources")

pbj_bm = BM()
obj_ferari = Ferari()
for car in (pbj_bm, obj_ferari):
    car.mileage()
    car.max_speed()
    car.type()