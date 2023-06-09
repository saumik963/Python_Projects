from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, name, email, password):
        self.email = email
        self.password = password
        self.name = name


class User(Account):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__balance = 0
        self.history = []

    def deposit(self, amount):
        self.__balance += amount
        b.bank_capital += amount
        self.history.append(f"Deposit: +{amount}.")

        print(
            f"{self.name}:: Deposit {amount} TK successful. Current balance {self.__balance}")

    def withdraw(self, amount):
        if self.__balance > amount < b.bank_capital:
            self.__balance -= amount
            b.bank_capital -= amount
            print(
                f"{self.name} :: Withdraw {amount} TK successful. Current balance {self.__balance}")
            self.history.append(f"Withdraw: -{amount}.")
        else:
            print("Bank is Bankrupt")

    def check_balance(self):
        print(f"{self.name} :: Your current balance is : {self.__balance}")
        return ''

    def transfer(self, to_who, amount):
        if amount < self.__balance:
            to_who.__balance += amount
            self.__balance -= amount
            print(
                f"{self.name} :: You successfully transfer to {to_who.name} account, Amount: {amount}")
            self.history.append(f"Transfer -{amount} to {to_who.name}")
            to_who.history.append(
                f"Received from {self.name}, Amount: +{amount}")

        else:
            print(f"{self.name} :: You don't have enough balance in your account to transfer.")

    def tra_history(self):
        print(f"________Showing Transaction History :: {self.name}________")
        for h in self.history:
            print(h)

    def take_loan(self):
        if b.lone_on_off == True:
            loan = self.__balance * 2
            if loan < b.bank_capital:
                self.__balance += loan
                b.total_loan += loan
                self.history.append(f"Take Loan +{loan} TK.")
                print(f"{self.name} :: You get {loan} TK loan.")

            else:
                print("Bank is Bankrupt.")
        else:
            print("Loan feature is currently off. Try again leter.")


class Admin(Account):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def check_capital(self):
        print(f"Available balance in the Bank is {b.bank_capital}")

    def check_lone(self):
        print(f"Total loan given by the Bank {b.total_loan}")

    def lone_feture(self, on_of):
        if on_of == 1:
            b.lone_on_off = True
        elif on_of == 0:
            b.lone_on_off = False


class Bank:

    def __init__(self):
        self.users = []
        self.admins = []
        self.total_loan = 0
        self.bank_capital = 0
        self.lone_on_off = True

    def create_user(self, user_name, email, password):
        user = User(user_name, email, password)
        self.users.append(user)
        print("User account created.", user.name)
        return user

    def create_admin(self, admin_name, email, password):
        admin = Admin(admin_name, email, password)
        self.admins.append(admin)
        print("Admin account created.", admin.name)
        return admin


print("________Creating accounts________")
b = Bank()
peter = b.create_user("Peter Parker", "peter@parker.com", "asdf")
jems = b.create_user("Jems Bond", "jems007@bond.con", "fdaas")

adm = b.create_admin("Will Smit", "brac@bank.com", "trweq")

print("\n_________Banking________")

adm.lone_feture(1)
peter.deposit(10000)
jems.deposit(50000)

peter.take_loan()
jems.withdraw(5000)
jems.transfer(peter, 3000)
peter.transfer(jems, 33000)

adm.lone_feture(0)
jems.take_loan()
print("________________________")
peter.check_balance()
jems.check_balance()
print("________________________\n")

adm.check_capital()
adm.check_lone()
print()

jems.tra_history()
peter.tra_history()
