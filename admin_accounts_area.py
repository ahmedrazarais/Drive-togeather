# Description: This file contains the functions for the admin accounts area.
account_sep="#@!%^"             # SEPERATOR


# Admin choices for accounts section
def admin_choices_accounts():
    print("\t\tWelcome To Admin Accounts Section")
    print("\t1.View All Users Accounts.")
    print("\t2.Add any user account.")
    print("\t3.search any user account.")
    print("\t4.Exit: To Exit From Accounts Section.")
    print()

# View all users accounts
def view_all_users_accounts(file_accounts):
    try:     # Try to open the file
        with open(file_accounts, "r") as accounts:
            lines = accounts.readlines()
            if not lines:  # Check if the file is empty
                print()
                print("No user accounts information received yet.")
                print()
            else:   # If the file is not empty, print the user accounts
                print()
                print("\tHere Are The User Accounts.")
                print()
                print("{:<15} {:<15} {:<15}".format("Username", "Password","securityanswer"))
                print("="*60)  # Separator line
                for line in lines:
                    # Split the line into parts
                    parts = line.strip().split(account_sep)

                    if len(parts) >= 2:  # Check if there are at least 2 parts
                        username, password , securityanswer= parts[:3]  # Take only the first two parts
                        print("{:<15} {:<15} {:<15}".format(username, password,securityanswer))

                    else:
                        print(f"Invalid data format: {line.strip()}")  # Print error message for invalid data
    # If the file is not found, print an error message
    except FileNotFoundError:
        print("User accounts file not found.")






# Search user account
def search_user_account(file_accounts, accounts_users):
    while True:
        with open(file_accounts, "r") as accounts:
            lines = accounts.readlines()
            if not lines:  # Check if the file is empty               
                print("No user accounts information received yet.")
                return    # return from function if file is empty
            
            # If the file is not empty, ask the user for the username to search
            else:
                username = input("Enter the username of the account to search (enter 0 to back): ")
                if username == "0": 
                    print("Back From Search Account Section.")
                    print()
                    return
                # If the username is not empty, search for the username in the file
                found = False

                
                with open(file_accounts, "r") as accounts:
                    lines = accounts.readlines()
                    for line in lines:
                        parts = line.strip().split(account_sep)
                        if len(parts) >= 2:

                            # Check if the username is found
                            if parts[0] == username:
                                found = True   
                                # if found then, print that username password and security answer
                                print()
                                print(f"Account with username {username} found.")
                                print(f"Username: {parts[0]}")
                                print(f"Password: {parts[1]}")
                                print(f"Security Answer: {parts[2]}")
                                print()
                                break
                    if found:
                        return    # return from function if username found after printing its details

                # If the username is not found, print an error message
                if not found:
                    print("Username not found.Please Enter Correct Username.")
                    print()