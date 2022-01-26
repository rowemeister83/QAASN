import os

class Budget:
    
    def __init__(self, name):
        os.system('cls')
        self.name = name
        self.balance = 0

    def deposit(self, amount):
         self.balance = amount
         
         return (f"Your new balance is {self.balance} in {self.name} budget")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("********** Transaction Failed **********")
            print("Insufficient funds")          
            
        else:
            self.balance = self.balance - amount
            result = ("********** Successful Transaction **********\n")
            result += (f"Your new balance is {self.balance} in {self.name} budget")
            
            return result

    def get_balance(self):
        balance = (f"The balance for {self.name} is {self.balance}")
        return balance
    
    def transfer(self, amount, category):
        if self.name == category.name:
            result = ("ERROR!\n")
            result += ("You cannot transfer funds within the same category\n")
            result += ("You can only transfer funds to another category")
            return result
        
        else:
            if self.balance < amount:
                print("********** Transaction Failed **********")
                print("Insufficient funds")
            else:
                self.balance -= amount
                category.balance += amount
            
                trans_result = ("********** Successful Transaction **********\n")
                trans_result += (f"The balance for the {self.name} budget is {self.balance}\n")
                trans_result += (f"The balance for the {category.name} budget is {category.balance}")
            
                return trans_result


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

food.deposit (10000)
clothing.deposit(5000)
                 
                 
print(food.transfer(5000, food))
