def show_balance(balance):
    print("Your current balance is: $" + str(balance))


def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance += amount
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    return balance - float(amount)


def logout(name):
    print("Goodbye " + name + "! Have a great day! :D")
