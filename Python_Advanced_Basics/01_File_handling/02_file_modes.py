f = open("student.txt" , "r")
data = f.read()
print(data)
f.close()

f =open("student.txt" , "a")
f.write("everest engineering college")
f.close()

f =open("sample.txt" , "w")
f.write("this is a sample file")
f.close()

