class  India():
    def capital(self):
        print("New delhi is the capital city of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")

class  USA():
    def capital(self):
        print("Washington , D.C. is the capital of USA")
    def language(self):
        print("Emglish is the primary language of USA")
    def type(self):
        print("USA is a developing country")

pbj_ind = India()
obj_Usa = USA()
for country in (pbj_ind, obj_Usa):
    country.capital()
    country.language()
    country.type()