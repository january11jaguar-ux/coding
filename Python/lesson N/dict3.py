country_cod = {'India' : '0091' , 'Australia' : '0025' , 'Nepal' : '00997'}

#Search dictionary for country code India
print ("country code for India - ")
print(country_cod.get('India' , 'Not found'))

#Search dictionary for country code Japan
print ("country code for Japan - ")
print(country_cod.get('Japan' , 'Not found'))