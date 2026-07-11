#create class
class IOstring():
   #constructor to set default value
    def __init__(self):
        self.str1 = ""
 # function to get input
    def get_string(self):
        self.str1 = input("Enter a string : ")

    def print_string(self):
        print("Result is : ", self.str1.upper())

str1 = IOstring()

str1.get_string()
str1.print_string()