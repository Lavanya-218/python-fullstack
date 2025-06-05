from abc import ABC , abstractmethod
customer={}
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withDraw(self):
        pass

class SavingAccount(Account):
    __balance = 0
    def get_balance(self):
        return self.__balance

    def deposit(self):
        self.amount=int(input("Enter the amount to be deposited:"))
        self.__balance += self.amount
        print("Deposited Amount: ", self.amount)

    def withDraw(self):
        self.amount=int(input("Enter the amount to be withdrawn:"))
        if self.__balance < self.amount:
            print("Not Enough Balance")
            return   
        self.__balance -= self.amount
        print("Withdrawn Amount : " , self.amount)


class CurrentAccount(Account):
    __balance = 0
    withDraw_limit = 0
    def __init__(self , limit):
        self.withDraw_limit = limit

    def get_balance(self):
        return self.__balance

    def deposit(self):
        self.amount=int(input("Enter the amount to be deposited:"))
        self.__balance += self.amount
        print("Deposited Amount: ", self.amount)

    def withDraw(self):
        self.amount=int(input("Enter the amount to be withdrawn:"))
        if self.__balance + self.withDraw_limit < self.amount:
            print("Not Enought Balance")
            return
        self.__balance -= self.amount
        customer[self.amount]
        print("Withdrawn Amount : " , self.amount)



class Bank:

    owner = "bank"
    account_number = 0

    def __init__(self):
        self.owner = input("Enter the owner name: ")
        self.account_number = int(input("Enter the account number:"))
        self.account_type=input("Enter the account type (Saving/Current):")
        #customer[self.account_number]=self.owner,self.account_number,self.account_type

        if self.account_type == "Saving":
            self.account = SavingAccount()
        if self.account_type == "Current":
            self.account = CurrentAccount(5000)
        customer= {
            "name": self.owner,
            "Account Number" : self.account_number,
            "account_type": self.account_type,
            "balance": self.account.get_balance()
        }
    def write_data(self):
        file=open("day_8/bank.txt","a")
        #file.write(f"name": {self.owner}"Account Number" : {self.account_number}"account_type":{ self.account_type}"balance": {self.account.get_balance()})


class Manager:

    def get_customer_info(self , bankAccount : Bank):
        print(f"Name : {bankAccount.owner}")
        print(f"AccountNumber : {bankAccount.account_number}")
        print(f"Account Type : {"Savings Account" if type(bankAccount.account) == SavingAccount else "Current Account"}")
        print(f"Balance : {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object"

man=Manager()
while True:
    try:
        print("Choice\n")
        print("1.Create Account")
        print("2.To Deposit money")
        print("3.To Withdrawn money")
        print("4.To view Customer details")
        print("5.To view all the customer details")
        print("5.Exit")
        choice=int(input("Enter the choice:"))
        if choice==1:
            bank=Bank()
            print("Account Created successfully")
        elif choice==2:
            customer["balance"]=bank.account.deposit()
            print("Money deposited")
        elif choice==3:
            customer['balance']=bank.account.withDraw()
            print("Money Withdrawn")
        elif choice==4:
            man=Manager()
            man.get_customer_info(bank)
        else:
            print(customer)
            print("Thank You")
            break



    except Exception as e:
        print(e)
