#Use XOR to check a value the user entered to see if it's an odd

clues = [3, 5, 3, 5, 9]
xor_res = 0

for clue in clues:
    xor_res = xor_res ^ clue

print("\nPART 2: XOR Cancellation")
print("Clues:", clues)
print("Final XOR Result:", xor_res)
print("Repeated clues cancel out, so the remaining clue is:", xor_res)