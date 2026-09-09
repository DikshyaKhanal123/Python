class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self): #getter 
        return self.__balance
    
    def set_balance(self,newBalance): #setter
        self.__balance = newBalance

acc1 = BankAccount("dikshya" , 14000)
#print(acc1.name, acc1.balance) not access 

print(acc1.get_balance())
acc1.set_balance(3000)
print(acc1.get_balance())