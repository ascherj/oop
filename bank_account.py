class BankAccount:
    """
    A class to represent a bank account with basic banking operations.

    Attributes:
        accountNumber (str): A unique identifier for the account
        balance (float): The current amount of money in the account
        accountHolder (str): The name of the person who owns the account
        interestRate (float): The annual interest rate (e.g., 0.02 for 2%)
        isActive (bool): Whether the account is currently active
    """

    def __init__(self, account_number, account_holder, initial_balance=0.0, interest_rate=0.0):
        """
        Initialize a new BankAccount instance.

        Args:
            account_number (str): Unique identifier for the account
            account_holder (str): Name of the account owner
            initial_balance (float): Starting balance (default: 0.0)
            interest_rate (float): Annual interest rate (default: 0.0)
        """
        self.accountNumber = account_number
        self.balance = initial_balance
        self.accountHolder = account_holder
        self.interestRate = interest_rate
        self.isActive = True

    def deposit(self, amount):
        """
        Adds money to the balance.

        Args:
            amount (float): Amount to deposit

        Returns:
            bool: True if deposit successful, False otherwise
        """
        if not self.isActive:
            print("Account is closed. Cannot perform transactions.")
            return False

        if amount <= 0:
            print("Deposit amount must be positive.")
            return False

        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Removes money from the balance if sufficient funds are available.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if not self.isActive:
            print("Account is closed. Cannot perform transactions.")
            return False

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def calculateInterest(self):
        """
        Calculates and adds interest to the balance based on the interest rate.
        """
        if not self.isActive:
            print("Account is closed. Cannot calculate interest.")
            return

        interest = self.balance * self.interestRate
        self.balance += interest
        print(f"Interest calculated: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def closeAccount(self):
        """
        Sets isActive to false and prevents further transactions.
        """
        self.isActive = False
        print(f"Account {self.accountNumber} has been closed.")

    def getBalance(self):
        """
        Returns the current balance.

        Returns:
            float: Current account balance
        """
        return self.balance

    def __str__(self):
        """
        String representation of the BankAccount.

        Returns:
            str: Formatted account information
        """
        status = "Active" if self.isActive else "Closed"
        return (f"Account Number: {self.accountNumber}\n"
                f"Account Holder: {self.accountHolder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Interest Rate: {self.interestRate*100:.2f}%\n"
                f"Status: {status}")


# Example usage
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("ACC001", "John Doe", 1000.0, 0.02)

    # Display account info
    print("Initial Account Information:")
    print(account)
    print()

    # Perform some transactions
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: ${account.getBalance():.2f}")
    print()

    # Calculate interest
    account.calculateInterest()
    print()

    # Close account
    account.closeAccount()

    # Try to perform transaction on closed account
    account.deposit(100)
