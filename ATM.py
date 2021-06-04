# Create Account
bank_accounts = {}
counter = 2


def register():
    if bank_accounts:

        name = input("Enter your name: ")
        account_num = input("Enter account number: ")
        user_pin = input("Enter your 4 digit pin: ")

        if user_pin in bank_accounts.keys() or account_num in bank_accounts.values() or name in bank_accounts.values():
            print('==========================')
            print('Data already exist, please try again!')
        else:
            for record in bank_accounts.values():
                if account_num in record.values() or name in record.values():
                    print('Data already exist, please try again!')
                else:
                    bank_accounts[user_pin] = {
                        "Name": name, "Account": account_num, "Pin": user_pin,"Balance": 0}
                    print('Data recorded!')
                    print(bank_accounts.values())
                    print('========================')
                    break
    else:
        name = input("Enter your name: ")
        account_num = input("Enter account number: ")
        user_pin = input("Enter your 4 digit pin: ")
        bank_accounts[user_pin] = {
            "Name": name, "Account": account_num, "Pin": user_pin, "Balance": 0}
        print(bank_accounts)
        print('==========================')


def deposit(pin, amount):
    if pin in bank_accounts.keys():
        bank_accounts[pin]['Balance'] += amount
    else:
        print('Invalid Pin!')
        print('========================')


def withdraw(pin, amount):
    if pin in bank_accounts.keys():
        if bank_accounts[pin]['Balance'] > amount:
            bank_accounts[pin]['Balance'] -= amount
        else:
            print('Insufficient Balance!')
    else:
        print('Invalid Pin!')
        print('========================')


def balance(pin):
    if pin in bank_accounts.keys():
        print('Your balance is: ', bank_accounts[pin]['Balance'])
    else:
        print('Invalid pin or pin does not exist!')
        print('=========================')


def transfer(pin, account, amount):
    if pin in bank_accounts.keys():
        if bank_accounts[pin]['Balance'] > amount:
            withdraw(pin, amount)
        else:
            print('Insufficient Balance!')
        for record in bank_accounts.values():
            if account in record.values():
                bank_accounts[record['Pin']]['Balance'] += amount
                print('===================================')
                print('Tranfer made to ', account, ' was successful!')
                print(bank_accounts)
                break
    else:
        print('Record not found')


def main():
    runtime = 1
    print('Welcome to MTS Bank')
    while runtime:
        checker = int(input(
            'Enter 0 to register, 1 for balance, 2 for deposit, 3 for withdrawal, 4 for transfer, and 5 to quit: '))

        if checker == 0:
            register()
        elif checker == 1:
            pin = input('Please enter your pin to check balance: ')
            balance(pin)
        elif checker == 2:
            pin = input('Please enter your pin: ')
            amount = int(input('Enter amount to deposit: '))
            deposit(pin, amount)
        elif checker == 3:
            pin = input('Please enter your pin: ')
            amount = int(input('Enter amount to withdraw: '))
            withdraw(pin, amount)
        elif checker == 4:
            pin = input('Please enter your pin: ')
            amount = int(input('Enter amount to transfer: '))
            account = input('Enter account to transfer to: ')
            transfer(pin, account, amount)
        elif checker == 5:
            break
        else:
            print('Invalid value, try again')
            main()


main()
