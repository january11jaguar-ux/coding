class SRev:
    def __init__(self, text):
        self.text = text
    def reverse_words(self):
        return ''.join(self.text [::-1])

input_text = input ("Enter a string : ")
reverser = SRev(input_text)
rtext = reverser.reverse_words()
print(rtext) 