from decimal import Decimal
from beancounter.basics.transaction import Deposit, Bill

# TODO: Add transfers to accounts
# TODO: Record transfers on recorded_balance
class Account:
    """
    Represents an account (a place to keep cash)
    """

    def __init__(self, name):
        self._name = name
        self._balance = Decimal('0.00')
        self._initial_balance = self._balance
        self._transactions = []

    def name(self):
        """Returns Account name"""
        return self._name

    def balance(self):
        """Returns the current balance"""
        return self._balance

    def transactions(self):
        """Returns list of transactions entered for this account"""
        return self._transactions

    def __str__(self):
        return "Account({name})".format(name=self._name)

    def __repr__(self):
        return "Account({name}, balance={balance})".format(
            name=self._name, balance=repr(self._balance)
        )

    def register(self, transaction):
        """
        Registers a transaction, updating the account balance
        :param transaction:
        """
        self._transactions.append(transaction)
        self._balance += transaction.balance_change()

    def deposit(self, amount, deposit_date):
        """
        Deposit money to the account
        :param amount: amount, right? Make it Decimal
        """
        deposit = Deposit(amount, deposit_date)
        self.register(deposit)
        return deposit

    def bill(self, amount, bill_date):
        """
        Deposit money to the account
        :param amount: amount, right? Make it Decimal
        """
        bill = Bill(amount, bill_date)
        self.register(bill)
        return bill

    def recorded_balance(self):
        """
        Recorded balance - a balance of an account that includes only recorded transactions
        :return: recorded account balance
        """
        recorded_change = sum(t.balance_change() for t in self._transactions if t.is_recorded())
        return self._initial_balance + recorded_change
