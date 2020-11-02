"""
Lab 7
Ken Zhang
CS 166 / Fall 2020

Create a login and menu to a company intranet system that requires users (employees)
to enter a username and password in order to view a menu of options
(such as Time Reporting, Accounting, IT Helpdesk, Engineering Documents, etc.).
"""

import sys


def main():
    """Main function"""
    # Print head
    print('Welcome to CatCoin!"')
    print('Please select from the following options:')
    print('    1. Check Wallet Balance')
    print('    2. Transfer CatCoins')
    print('    3. Quit CatCoin')
    choice = input('')
    while choice == 1 or 2 or 3:
        if choice == 1:
            check_balance()
        elif choice == 2:
            transfer()
        elif choice == 3:
            sys.exit()
        else:
            choice = input(print('Invalid input. Try again: '))


def check_balance():
    print()


def transfer():
    print()





main()