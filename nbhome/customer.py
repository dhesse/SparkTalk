class Customer(object):
    def __init__(self, balance=0, transactions=[]):
        self.balance = balance
        self.transactions = transactions
        if self.balance > 0:
            self.transactions.append(balance)
    def deposit(self, ammount):
        self.balance += ammount
        self.transactions.append(ammount)
        return self
