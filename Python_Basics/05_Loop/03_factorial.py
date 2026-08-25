num = int(input("enter number"))
i = 1
factorial = 1

while i <= num:
    factorial = factorial * i
    i += 1

print("Factorial =", factorial)