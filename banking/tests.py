from django.test import TestCase
from .models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        # This runs before every test. Let's create our test account here.
        self.account = Account.objects.create(name="Juan")
        self.account.set_balance(1000.0)

    def test_display_info(self):
        self.assertEqual(self.account.display_info(), "Account of Juan has balance 1000")

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0)

    def test_valid_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.get_balance(), 800.0)

    def test_invalid_withdraw(self):
        # We expect a ValueError if Juan tries to withdraw more than his balance
        with self.assertRaises(ValueError):
            self.account.withdraw(5000.0)
            
    def test_invalid_set_balance(self):
        # We expect a ValueError if we try to set a negative balance
        with self.assertRaises(ValueError):
            self.account.set_balance(-50.0)
            
    def test_negative_withdraw(self):
        # We expect a ValueError if we try to withdraw a negative number
        with self.assertRaises(ValueError):
            self.account.withdraw(-50.0)
