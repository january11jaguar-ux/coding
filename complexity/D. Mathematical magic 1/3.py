def roman_Int(romaninput):

    roman = {'M': 1000, 'D': 500,'C':100 ,'L': 50,'X':10,'V':5,'I':1}

    resultInt = 0

    for i in range(0, len(romaninput) - 1):
        if roman[romaninput[i]] < roman[romaninput[i+1]]:
            resultInt -= roman[romaninput[i]]
        else:
            resultInt += roman [romaninput[i]]
    return resultInt + roman[romaninput[-1]]

roman = input("Input roman numeral : ").upper()

print("Interger equivalent : ", roman_Int(roman))