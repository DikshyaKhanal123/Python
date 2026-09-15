#normal list

square = []
for i in range(6):
    square.append(i*i)

print(square)

#list comprehensions

squares = [i*i for i in range(6)]
print(squares)

#sqaure of odd numbers only 
sq_odd = [i*i for i in range(6) if i%2 != 0]
print(sq_odd)
