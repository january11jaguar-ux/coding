number = int(input("Enter your number: "))

original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10

if original_number == reverse_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")