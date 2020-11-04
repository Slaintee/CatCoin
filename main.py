"""
Lab 7
Ken Zhang
CS 166 / Fall 2020
"""

import csv
import sys


def main_menu():
    """
    Menu function
    :returns: the secondary menu, two functions and exit
    """
    print('Please select from the following options:')
    print('    1. Check Wallet Balance')
    print('    2. Transfer CatCoins')
    print('    3. Quit CatCoin')
    choice = input()
    while choice != '1' and choice != '2' and choice != '3':
        print('Invalid input. Try again: ')
        choice = input()
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
    """
    Function to check balance from wallet.csv
    :return: balance
    """
    print('Which account would you like to check? (1/2/3)')
    account_number = input()
    while account_number != '1' and account_number != '2' and account_number != '3':
        print('Invalid input. Try again: ')
        account_number = input()
    with open('wallet.csv', 'r') as f:
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
        print('Invalid input. Try again: ')
        check_other = input()
    if check_other == '1':
        check_balance()
    else:
        print('-----------------------------------------')
        main_menu()


def transfer():
    """
    Function to transfer coin from a wallet to another
    :return: revised wallet.csv
    """
    # Open CSV and save amount in dictionary
    balance_dict = {}
    with open('wallet.csv', 'r') as f:
        balance_line = f.readlines()[1:]
        for line in balance_line:
            bal = line.split(',')
            wallet = bal[0]
            balance = bal[1]
            balance = "".join(balance).replace('\n', '')
            balance_dict[wallet] = float(balance)
    # Choose two wallets
    print('Choose a source wallet 1/2/3: ')
    source = input()
    while source != '1' and source != '2' and source != '3':
        print('Invalid input. Try again: ')
        source = input()
    print('Choose a destination wallet 1/2/3: ')
    destination = input()
    while destination != '1' and destination != '2' and destination != '3' and destination == source:
        print('Invalid input. Try again: ')
        destination = input()
    # Input amount
    try:
        print('Transfer amount: ')
        amount = float(input())
    except ValueError:
        print('Invalid input. Try again: ')
        amount = float(input())
    if amount <= 0:
        print('Invalid amount.')
        print('-----------------------------------------')
        main_menu()
    else:
        print('Are you sure you want to transfer', amount, 'CatCoins to Wallet', destination, '? y/n')
        decision = input()
        if decision == 'y' or decision == 'Y':
            if amount > balance_dict[source]:
                print('Insufficient balance.')
                print('-----------------------------------------')
                main_menu()
            else:
                # Make changes and write to csv file
                balance_dict[source] -= amount
                balance_dict[destination] += amount
                header = ['wallet number', 'balance']
                data = [{'wallet number': '1', 'balance': balance_dict['1']},
                        {'wallet number': '2', 'balance': balance_dict['2']},
                        {'wallet number': '3', 'balance': balance_dict['3']}]
                with open('wallet.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(data)
        print('Transaction complete')
        print('-----------------------------------------')
        main_menu()


def main():
    """Main function"""
    # Print head
    print('Welcome to CatCoin!"')
    main_menu()


main()
