import unittest
from BankingSystem import BankingSystem


class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.banking_system = BankingSystem()

    def test_01_createAccount_success(self):
        account_number = self.banking_system.createAccount("John Doe", 100.0)
        self.assertIsNotNone(account_number)
        self.assertIsInstance(account_number, str)
        # Test that account can be used for operations
        balance = self.banking_system.deposit(account_number, 50.0)
        self.assertEqual(balance, 150.0)

    def test_02_createAccount_zero_initial_amount(self):
        account_number = self.banking_system.createAccount("Jane Smith", 0)
        self.assertIsNotNone(account_number)
        # Test that account starts with zero balance
        balance = self.banking_system.deposit(account_number, 100)
        self.assertEqual(balance, 100)

    def test_03_createAccount_multiple_accounts(self):
        account1 = self.banking_system.createAccount("John Doe", 100)
        account2 = self.banking_system.createAccount("Jane Smith", 200)
        # Accounts should be different
        self.assertNotEqual(account1, account2)
        # Both accounts should work independently
        balance1 = self.banking_system.deposit(account1, 50)
        balance2 = self.banking_system.withdraw(account2, 100)
        self.assertEqual(balance1, 150)
        self.assertEqual(balance2, 100)

    def test_04_createAccount_large_initial_amount(self):
        account_number = self.banking_system.createAccount("Rich Person", 1000000.99)
        # Verify by depositing and checking new balance
        balance = self.banking_system.deposit(account_number, 0.01)
        self.assertEqual(balance, 1000001.0)

    def test_05_createAccount_float_amount(self):
        account_number = self.banking_system.createAccount("Test User", 123.45)
        # Verify initial balance by withdrawing exact amount
        balance = self.banking_system.withdraw(account_number, 123.45)
        self.assertEqual(balance, 0)

    def test_06_createAccount_name_preservation(self):
        special_name = "O'Connor-Smith Jr."
        account_number = self.banking_system.createAccount(special_name, 100)
        # Name preservation can only be tested if implementation exposes it
        # Here we just verify account creation succeeded
        self.assertIsNotNone(account_number)

    def test_07_createAccount_name_with_numbers(self):
        account_number = self.banking_system.createAccount("User123", 100)
        self.assertIsNotNone(account_number)

    def test_08_createAccount_very_long_name(self):
        long_name = "A" * 100
        account_number = self.banking_system.createAccount(long_name, 100)
        self.assertIsNotNone(account_number)

    def test_09_createAccount_trimmed_spaces(self):
        account_number = self.banking_system.createAccount("  John Doe  ", 100)
        self.assertIsNotNone(account_number)

    def test_10_createAccount_sequential_creation(self):
        accounts = []
        for i in range(5):
            account = self.banking_system.createAccount(f"User{i}", 100)
            accounts.append(account)
        # All accounts should be unique
        self.assertEqual(len(set(accounts)), 5)

    def test_11_deposit_success(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.deposit(account_number, 50)
        self.assertEqual(new_balance, 150)

    def test_12_deposit_large_amount(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.deposit(account_number, 999999.99)
        self.assertEqual(new_balance, 1000099.99)

    def test_13_deposit_small_decimal_amount(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.deposit(account_number, 0.01)
        self.assertEqual(new_balance, 100.01)

    def test_14_deposit_multiple_times(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        self.banking_system.deposit(account_number, 25)
        self.banking_system.deposit(account_number, 30)
        new_balance = self.banking_system.deposit(account_number, 45)
        self.assertEqual(new_balance, 200)

    def test_15_deposit_to_zero_balance_account(self):
        account_number = self.banking_system.createAccount("John Doe", 0)
        new_balance = self.banking_system.deposit(account_number, 100)
        self.assertEqual(new_balance, 100)

    def test_16_withdraw_success(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.withdraw(account_number, 30)
        self.assertEqual(new_balance, 70)

    def test_17_withdraw_exact_balance(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.withdraw(account_number, 100)
        self.assertEqual(new_balance, 0)

    def test_18_withdraw_small_decimal_amount(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        new_balance = self.banking_system.withdraw(account_number, 0.01)
        self.assertEqual(new_balance, 99.99)

    def test_19_withdraw_multiple_times(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        self.banking_system.withdraw(account_number, 25)
        self.banking_system.withdraw(account_number, 30)
        new_balance = self.banking_system.withdraw(account_number, 45)
        self.assertEqual(new_balance, 0)

    def test_20_withdraw_exactly_one_cent_remaining(self):
        account_number = self.banking_system.createAccount("John Doe", 100.01)
        new_balance = self.banking_system.withdraw(account_number, 100)
        self.assertAlmostEqual(new_balance, 0.01, places=2)

    def test_21_multiple_operations_sequence(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        balance1 = self.banking_system.deposit(account_number, 50)
        self.assertEqual(balance1, 150)
        balance2 = self.banking_system.withdraw(account_number, 25)
        self.assertEqual(balance2, 125)
        balance3 = self.banking_system.deposit(account_number, 75)
        self.assertEqual(balance3, 200)

    def test_22_alternating_deposits_and_withdrawals(self):
        account_number = self.banking_system.createAccount("John Doe", 100)
        final_balance = 100
        for i in range(5):
            self.banking_system.deposit(account_number, 10)
            final_balance += 10
            balance = self.banking_system.withdraw(account_number, 5)
            final_balance -= 5
        self.assertEqual(balance, final_balance)

    def test_23_multiple_accounts_operations(self):
        acc1 = self.banking_system.createAccount("User1", 100)
        acc2 = self.banking_system.createAccount("User2", 200)
        acc3 = self.banking_system.createAccount("User3", 300)

        balance1 = self.banking_system.deposit(acc1, 50)
        balance2 = self.banking_system.withdraw(acc2, 100)
        balance3 = self.banking_system.deposit(acc3, 200)

        self.assertEqual(balance1, 150)
        self.assertEqual(balance2, 100)
        self.assertEqual(balance3, 500)

    def test_24_stress_test_many_accounts(self):
        accounts = []
        for i in range(10):
            account = self.banking_system.createAccount(f"User{i}", i * 10)
            accounts.append(account)
        # All accounts should be unique
        self.assertEqual(len(set(accounts)), 10)

    def test_25_stress_test_many_deposits(self):
        account_number = self.banking_system.createAccount("Test User", 0)
        for i in range(10):
            self.banking_system.deposit(account_number, 1)
        final_balance = self.banking_system.deposit(account_number, 0)
        self.assertEqual(final_balance, 10)

    def test_26_precision_test_float_operations(self):
        account_number = self.banking_system.createAccount("Test User", 10.50)
        self.banking_system.deposit(account_number, 5.25)
        new_balance = self.banking_system.withdraw(account_number, 3.33)
        self.assertAlmostEqual(new_balance, 12.42, places=2)

    def test_27_edge_case_large_numbers(self):
        account_number = self.banking_system.createAccount("Rich User", 1e10)
        new_balance = self.banking_system.deposit(account_number, 1e10)
        self.assertEqual(new_balance, 2e10)

    def test_28_account_isolation_test(self):
        acc1 = self.banking_system.createAccount("User1", 100)
        acc2 = self.banking_system.createAccount("User2", 100)

        balance1 = self.banking_system.deposit(acc1, 50)
        balance2 = self.banking_system.withdraw(acc2, 30)

        self.assertEqual(balance1, 150)
        self.assertEqual(balance2, 70)

    def test_29_balance_consistency_after_operations(self):
        account_number = self.banking_system.createAccount("Test User", 1000)
        operations = [
            ('deposit', 100), ('withdraw', 50), ('deposit', 200),
            ('withdraw', 150), ('deposit', 75), ('withdraw', 25)
        ]

        for operation, amount in operations:
            if operation == 'deposit':
                self.banking_system.deposit(account_number, amount)
            else:
                self.banking_system.withdraw(account_number, amount)

        # Final operation to get current balance
        final_balance = self.banking_system.deposit(account_number, 0)
        expected_balance = 1000 + 100 - 50 + 200 - 150 + 75 - 25
        self.assertEqual(final_balance, expected_balance)

    def test_30_return_value_consistency(self):
        account_number = self.banking_system.createAccount("Test User", 100)

        deposit_result = self.banking_system.deposit(account_number, 50)
        # Verify consistency by doing another operation
        withdraw_result = self.banking_system.withdraw(account_number, 25)

        self.assertEqual(deposit_result, 150)
        self.assertEqual(withdraw_result, 125)

    def test_31_account_number_type_consistency(self):
        account_number = self.banking_system.createAccount("Test User", 100)
        self.assertIsInstance(account_number, str)

        for i in range(5):
            acc = self.banking_system.createAccount(f"User{i}", 100)
            self.assertIsInstance(acc, str)

    def test_32_empty_banking_system_state(self):
        empty_system = BankingSystem()
        # Should be able to create accounts immediately
        account = empty_system.createAccount("First User", 100)
        self.assertIsNotNone(account)

    def test_33_comprehensive_workflow_test(self):
        acc1 = self.banking_system.createAccount("Alice", 1000)
        acc2 = self.banking_system.createAccount("Bob", 500)
        acc3 = self.banking_system.createAccount("Charlie", 0)

        self.banking_system.deposit(acc1, 500)
        self.banking_system.withdraw(acc1, 200)
        self.banking_system.deposit(acc2, 300)
        self.banking_system.withdraw(acc2, 100)
        self.banking_system.deposit(acc3, 1000)
        balance3 = self.banking_system.withdraw(acc3, 250)

        # Verify final balances through operations
        final_balance1 = self.banking_system.deposit(acc1, 0)
        final_balance2 = self.banking_system.deposit(acc2, 0)

        self.assertEqual(final_balance1, 1300)
        self.assertEqual(final_balance2, 700)
        self.assertEqual(balance3, 750)

    def test_34_unicode_name_support(self):
        unicode_name = "José María González-López"
        account_number = self.banking_system.createAccount(unicode_name, 100)
        self.assertIsNotNone(account_number)


if __name__ == '__main__':
    unittest.main()