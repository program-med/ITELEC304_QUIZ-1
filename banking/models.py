from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0.0)

    def display_info(self):
        # Using :g formats floats beautifully, turning 1000.0 into 1000
        return f"Account of {self.name} has balance {self.get_balance():g}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
        else:
            raise ValueError("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")
        if amount <= self.get_balance():
            self._balance -= amount
            self.save()
        else:
            raise ValueError("Withdraw amount must be less than or equal to balance")

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
        else:
            raise ValueError("Balance cannot be negative")