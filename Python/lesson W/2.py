class Flashcard:
    def __init__(self,word,meaning):
        self.word =word
        self.meaning =meaning
    def __str__(self):
        return self.word + " ( "+ self.meaning + " ) "
    
flash = []
print("Welcome to Flashcard Application")
while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    flash.append(Flashcard(word,meaning))
    option = int(input("Enter 0 to add another flash card or 1 to stop: "))
    if option == 1:
        break

print("\nYour Flashcards")
for card in flash:
    print(">",card)