"""
Lab 7
Ken Zhang
CS 166 / Fall 2020


"""

import sys


def main_menu():
    print('Please select from the following options:')
    print('    1. Check Wallet Balance')
    print('    2. Transfer CatCoins')
    print('    3. Quit CatCoin')
    choice = input()
    while choice != '1' and choice != '2' and choice != '3':
        choice = input(print('Invalid input. Try again: '))
    if choice == '1':
        check_balance()
    elif choice == '2':
        transfer()
    else:
        print('Are you sure you want to exit CatCoin? y/n')
        to_exit = input()
        if to_exit == 'y' or to_exit == 'Y':
            sys.exit()
        else:
            main_menu()


def check_balance():
    print('Which account would you like to check? (1/2/3)')
    account_number = input()
    while account_number != '1' and account_number != '2' and account_number != '3':
        account_number = input(print('Invalid input. Try again: '))
    with open('balance.csv', 'r') as f:
        balance_line = f.readlines()
        for line in balance_line:
            bal = line.split(',')
            wallet = bal[0]
            balance = bal[1]
            balance = "".join(balance).replace('\n', '')
            if wallet == account_number:
                print('Balance: ', balance)
                break
    print('-----------------------------------------')
    print('Please select from the following options:')
    print('    1. Check Another Account Balance')
    print('    2. Return to Main Menu')
    check_other = input()
    while check_other != '1' and check_other != '2':
        check_other = input(print('Invalid input. Try again: '))
    if check_other == '1':
        check_balance()
    else:
        print('-----------------------------------------')
        main_menu()


def transfer():
    print()


def main():
    """Main function"""
    # Print head
    print('Welcome to CatCoin!"')
    main_menu()


main()
