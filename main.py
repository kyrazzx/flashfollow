import csv
import time
import os
import shutil
from colorama import Fore, Style, init
import scratchclient
from itertools import cycle

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art_with_animation():
    art = r"""
    _______________             ______ __________     ___________                
    ___  ____/__  /_____ __________  /____  ____/________  /__  /________      __
    __  /_   __  /_  __ `/_  ___/_  __ \_  /_   _  __ \_  /__  /_  __ \_ | /| / /
    _  __/   _  / / /_/ /_(__  )_  / / /  __/   / /_/ /  / _  / / /_/ /_ |/ |/ / 
    /_/      /_/  \__,_/ /____/ /_/ /_//_/      \____//_/  /_/  \____/____/|__/  
                                                                                
    """
    console_width = shutil.get_terminal_size().columns
    colors = cycle([Fore.RED, Fore.LIGHTRED_EX])

    for _ in range(10):
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)

    print(Fore.RED + "Made by Kyra".center(console_width))

def interactive_menu():
    while True:
        clear_console()
        print(Fore.RED + "Main Menu".center(shutil.get_terminal_size().columns, "-"))
        print(Fore.LIGHTRED_EX + "[1] Start Bulk Follow")
        print(Fore.LIGHTRED_EX + "[2] Exit")
        choice = input(Fore.RED + "Choose an option: ")
        if choice == "1":
            return
        elif choice == "2":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

def bulk_follow():
    target_username = input(Fore.LIGHTRED_EX + "Enter the username to follow: ")
    csv_file_path = input(Fore.LIGHTRED_EX + "Enter the path to the CSV file (username,password): ")
    time_interval = float(input(Fore.LIGHTRED_EX + "Enter the time interval between follows (in seconds): "))

    try:
        with open(csv_file_path, "r") as file:
            accounts = list(csv.reader(file))
    except FileNotFoundError    :
        print(Fore.RED + f"Error: File {csv_file_path} not found.")
        time.sleep(2)
        return

    print(Fore.LIGHTRED_EX + f"Detected {len(accounts)} accounts in the file.")

    for account in accounts:
        if len(account) != 2:
            print(Fore.RED + f"Invalid format for line: {account}. Skipping.")
            continue

        username, password = account
        print(Fore.LIGHTRED_EX + f"Attempting to log in with account: {username}")

        try:
            session = scratchclient.ScratchSession(username, password)
            target_user = session.get_user(target_username)

            print(Fore.GREEN + f"{username} is now following {target_username}.")
            target_user.follow()
            time.sleep(time_interval)

        except scratchclient.exceptions.InvalidUserCredentials:
            print(Fore.RED + f"Failed to log in for {username}: Invalid credentials.")
        except Exception as e:
            print(Fore.RED + f"Error for {username}: {e}")

    print(Fore.LIGHTRED_EX + "Bulk follow process completed.")
    time.sleep(2)

def main():
    clear_console()
    display_ascii_art_with_animation()
    time.sleep(1)
    interactive_menu()
    bulk_follow()

if __name__ == "__main__":
    main()