from src.UserManager import UserManager
from colorama import Fore, Style
import time

if __name__ == '__main__':
    manager = UserManager()
    switcher = True

    def info():
        print(f'{Fore.LIGHTYELLOW_EX + "\t" * 7 + "- Users -" + Fore.RESET}')
        [print(f'{Fore.LIGHTBLACK_EX + "#" * 70 + Fore.RESET}\n', manager.parse_users()[user]) for user in range(len(manager.fetch_users()))]

    info()
    time.sleep(1)

    while switcher:
        print('\n|1. More info about current user\n|2. Show all users\n|3. Exit\n')
        choice = input('Enter your choice: ')
        if choice == '1':
            try:
                user_id = int(input(f'Enter user id between {manager.fetch_users()[0]["id"]} and {len(manager.fetch_users())}: '))
                print(manager.more_info(user_id))
                time.sleep(1)
                input(Fore.LIGHTGREEN_EX + 'Press enter to continue...' + Fore.RESET)
            except Exception:
                print(Fore.LIGHTRED_EX + 'Invalid user id' + Fore.RESET)
                time.sleep(2)
        elif choice == '2':
            info()
        elif choice == '3':
            switcher = False
        else:
            print(Fore.LIGHTRED_EX + 'Something went wrong' + Fore.RESET)
            time.sleep(2)