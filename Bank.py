class User:
    def __init__(self, user_name, initial_balance=0):
        self.account_holder = user_name
        self.balance = initial_balance
        self.transactions = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn: {amount}")
        else:
            print("Bank is bankrupt.")

    def check_balance(self):
        print(f"{self.account_holder}'s balance is: {self.balance}")

    def transfer(self, amount, target_account):
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            self.transactions.append(f"Transferred: {amount} to {target_account.account_holder}")
            print(f"Transferred: {amount} to {target_account.account_holder}")
        else:
            print("Insufficient balance.")

    def check_transaction_history(self):
        print(f"{self.account_holder}'s transaction History: {self.transactions}")

    def take_loan(self):
        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.loan_taken += loan_amount
        self.transactions.append(f"Loan taken: {loan_amount}")
        return loan_amount


class Admin:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_on = True

    def create_account(self, user_name, initial_balance=0):
        account = User(user_name, initial_balance)
        self.accounts.append(account)
        self.total_balance += initial_balance
        return account

    def check_total_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts)
        return self.total_balance

    def check_total_loan_amount(self):
        self.total_loan_amount = sum(account.loan_taken for account in self.accounts)
        return self.total_loan_amount

    def set_loan_feature(self, status):
        self.loan_feature_on = status

#Create Admin
admin = Admin()

#Create 2 user with their name and priliminary deposit
Nayem = admin.create_account("Nayem", 350)
Jerin = admin.create_account("Jerin", 660)

#deposit
Nayem.deposit(250)
Nayem.check_balance()

Jerin.deposit(250)
Jerin.check_balance()

#withdraw
Nayem.withdraw(300)
Nayem.check_balance()
Jerin.withdraw(1500) #output: Bank is Bankcrupt
Jerin.check_balance()

#Transfer money
Nayem.transfer(200, Jerin)  # Successfull
Nayem.transfer(2000, Jerin) #UNsuccessful


#Loan
if admin.loan_feature_on:
    print(Nayem.take_loan())
    Nayem.check_balance()

# Admin turns off loan feature
admin.set_loan_feature(False)

if admin.loan_feature_on:   #it will not work because loan feature is off
    print(Nayem.take_loan())

#Transection History
Nayem.check_transaction_history()
Jerin.check_transaction_history()


# Admin checks total balance and total loan
print(f"Bank's Total Balance: {admin.check_total_balance()}")
print(f"Total Loan: {admin.check_total_loan_amount()}")