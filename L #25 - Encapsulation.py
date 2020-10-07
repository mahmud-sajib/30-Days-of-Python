## Day 25: Encapsulation

"""
Using OOP in Python, we can restrict access to methods and variables. 
This prevent data from direct modification which is called encapsulation. 
In Python, we denote private attribute using underscore as prefix i.e single "_" or double "__".
"""

# Simple class (Consider the below example. If we don't make our attributes private anyone can manipulate the 'balance')
class BankAccount():
    def __init__(self, acc_name, acc_balance):
        self.name = acc_name
        self.balance = acc_balance

obj1 = BankAccount("John Snow",2000)
print(obj1.balance) # output: 2000 (original balance)
obj1.balance = 150000 
print(obj1.balance) # output: 150000 (manipulated balance)

# Encapsulating the attributes (to prevent outside access)
class BankAccount():
    def __init__(self, acc_name, acc_balance):
        # private attributes
        self.__name = acc_name
        self.__balance = acc_balance

obj1 = BankAccount("John Snow",2000)
print(obj1.__balance) # output: AttributeError (since the attributes aren't accessible)

# Accessing the encapsulated attributes with Getters & Setters
class BankAccount():
    # private attributes
    def __init__(self, acc_name, acc_balance):
        self.__name = acc_name
        self.__balance = acc_balance

    # Getter
    def balanceGetter(self):
        print(f"Account name: {self.__name} - Original balance: {self.__balance}")
    
    # Setter
    def balanceSetter(self,bonus):
        self.__balance = self.__balance + bonus
        print(f"Account name: {self.__name} - Total balance incl. bonus {self.__balance}")

# instantiate object
customer_info = BankAccount("John Snow",2000)

# calling getter
customer_info.balanceGetter()

# calling setter
customer_info.balanceSetter(500)
