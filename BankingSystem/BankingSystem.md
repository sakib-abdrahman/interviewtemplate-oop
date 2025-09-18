# Banking System
Design and implement a simple Banking System. Your solution should include clean, extendable, and correct code that can handle the following requirements:

## Create Account
Create a new bank account with the given name and initial balance.
When an account is created, return a unique account number (string).
Multiple accounts should be supported and operate independently.

## Deposit Money
Given an account number and amount, deposit the specified amount into the account.
Return the new account balance after the deposit.
Only positive amounts should be allowed for deposits.

## Withdraw Money
Given an account number and amount, withdraw the specified amount from the account.
Return the new account balance after the withdrawal.
Prevent overdrafts: if insufficient funds are available, withdrawal should not succeed.
Only positive amounts should be allowed for withdrawals.