total = 0

for i in range(1, 15):
    marks = int(input(f"Enter marks for subject {i}: "))
    total += marks

print("Total marks =", total)