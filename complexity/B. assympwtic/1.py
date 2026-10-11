n = 10

guess = input("Double loop at n = 10 checks n x n pairs.  How many?  ")

input("Formula: one calculation, done. Press Enter to run ")
steps = 1
print("  steps =", steps, "  -> 0(1)  constant time  -> steps never change")

input("Loop: one step per item. Press Enter to run ")
steos = 0
for i in range(n):
    steps +=1
print("  steps =", steps, "  -> 0(n)  linear time  -> steps never change")

input("Double Loop: checks every pair. Press enter to run")
steps = 0
for i in range (n):
    for j in range(n):
        steps +=1
print("  steps =", steps,"  your guess:", guess, "  ->  0(n^2) quadratic time")

input("Tow more notations. Press Enter")
print("  Big Omega  ->  best case lower bound")
print("  Big Theta  -> exact bound (worst = best)")