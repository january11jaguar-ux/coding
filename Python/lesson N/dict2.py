# Initialize dictionary
test_dict = {'codingal':2, 'best':2,'for':2, 'coding' :1 }

#printing original dictionary
print ("The original dictionary : " + str(test_dict))

#Initialize value
k = 2

#Using loop
#Selective Key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key]==k:
        res = res + 1

#printing results
print("Frequency of k is : " + str(res))