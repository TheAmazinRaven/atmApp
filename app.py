from banking_pkg.account import *


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("Babeh that's invalid.")
        continue
    while True:
        pin = input("Enter PIN: ")
        if len(pin) > 4:
            print("Babeh that's invalid.")
            continue
        break
    break

balance = 0
print("Hello! " + name + ", your balance is $" + str(balance) + "!")

while True:
    nameToValidate = input("Enter your name! ")
    pinToValidate = input("Enter your pin! ")
    if name == nameToValidate and pin == pinToValidate:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials!")


while True:
    atm_menu(name)
    option = input(" Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
    elif option == "3":
        balance = withdraw(balance)
    else:
        logout(name)
        break
