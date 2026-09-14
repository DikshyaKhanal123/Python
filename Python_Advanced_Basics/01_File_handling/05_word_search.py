data = True
line = 1

with open("student.txt", "r") as f:
    while data:
        data = f.readline()
        
        if("Dikshya" in data):
            print("word found")
            break
        
        line += 1
