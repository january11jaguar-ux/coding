class pear_elements :

    def twosum(self, nums, target):

        lookup = {}

        for i, num in enumerate(nums):
           compliment = target - num 
           if compliment in lookup :
            return lookup [compliment],i
           lookup [num] = i
        return None
value = int(input("enter a sum of wich you want to make this search : "))
result = pear_elements().twosum((10,20,30,40,50,60,70),value)

if result :
   print("index1=%d,index2=%d" % result)
else :
   print ("The pair is not found")