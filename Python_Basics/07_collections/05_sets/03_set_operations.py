s1 = {"ram", "shyam", "hari" , "gopal"}
s2 = {"sita", "gita", "rita", "gopal"}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))

print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))