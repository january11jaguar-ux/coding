class NR :
    def convert(self, num):
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        rom = ""

        for i in range (len(value)):
            while num >=value[i]:
                rom += symbol [i]
                num -=value[i]
        return rom

number = int(input("Enter a number from (1-3999): "))
ob = NR()
print ("Your number is: ", ob.convert(number))