#without using continue
print("without using continue")
i = 1
while(i<=10):
    print(i)
    i += 2

#using continue 
print("using continue")
i =  1
while (i<=10):
    if(i%2 == 0 ):
        i += 1
        continue
  
    print(i)
    i += 1