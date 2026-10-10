w = 5

guess = input("Total laps around a small field:  10+ 15 + 20 + 10 =")

input("Formula: one calculation. Press Enter to run")
total = w * (w + 1)//2
print("  total = ", total, "  laps=", w)

input("loop: adds one lap at a time. Press Enter to run")
total=0
for laps in range(1, w +1):
    total += laps
print("  total =", total, "  laps=", w)