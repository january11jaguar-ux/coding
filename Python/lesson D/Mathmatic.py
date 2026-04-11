Amount = int(input("Enter the amount for withdrawler: "))
note1 = Amount//1000
note2 = (Amount%1000)//500
note3 = ((Amount%1000)%500)//200
note4=(((Amount%1000)%500)%200)//100
note5=((((Amount%1000)%500)%200)%100)//50

print("Note of KSH 1000 :",note1)
print("Note of KSH 500:",note2)
print("Note of KSH 200:",note3)
print("Note of KSH 100:",note4)
print("Note of KSH 50:",note5)