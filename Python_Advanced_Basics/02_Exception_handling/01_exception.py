try :
    x = int(input("enter x:"))
    ans = 10/x

except ZeroDivisionError:
    print("division by zero")

except ValueError:
    print("invalid input")

else:
    print(ans)

finally :
    print("end of program")