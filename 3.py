class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів на рахунку.")

    def __str__(self):
        return f"Власник: {self.owner}, Рахунок: {self.account_number}, Баланс: {self.balance} грн."


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(
                    f"Переказ {amount} грн з рахунку {from_account_number} на рахунок {to_account_number} успішно завершений.")
            else:
                print("Недостатньо коштів для переказу.")
        else:
            print("Один або обидва рахунки не знайдено.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print(f"Рахунок {account_number} не знайдено.")
        return None

    def __str__(self):
        return "\n".join([str(account) for account in self.accounts])


# Приклад використання
bank = Bank()

# Створюємо рахунки
account1 = BankAccount("Олег", "123456789", 1000)
account2 = BankAccount("Анна", "987654321", 500)

bank.add_account(account1)
bank.add_account(account2)

# Переказ коштів
bank.transfer("123456789", "987654321", 300)

# Виводимо інформацію про рахунки
print("\nІнформація про рахунки:")
print(bank)
