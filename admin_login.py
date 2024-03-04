from admin_accounts_area import admin_choices_accounts, view_all_users_accounts, search_user_account
from signup import sign_up
from admin_transport_area import admin_choices_vehicles, view_all_bookings, change_membership_status
from customer_area import display_car, display_bike, display_auto
from filespaths import  user_directory, member_directory, booking_file


# Admin login
def admin_login(file_accounts, accounts_users,  carfile, bikefile, autofile ):
    admin_username = "admin"    # Admin username
    admin_password = "admin123"   # admin password

    # Ask the user for the username and password
    while True:
        username = input("Enter Admin Username (enter 0 to back): ")
        if username == "0":
            return
        # Check if the username is correct
        if username == admin_username:
            break
        else:
            print("Incorrect Username")
            print()
    # when username is correct then ask for password
    while True:
            password = input("Enter Admin Password (enter 0 to back): ")
            if password == "0":
                return
            
            # Check if the password is correct
            if password == admin_password:
                print("Login Successful!!")
                print()
                break
            else:
                print("Incorrect Password")
                print()
    # open panel when username and password both are correct
    while True:         
        # Admin panel choices
            print("\t\tWelcome To Admin Section")  
            print("\t1. To Proceed To Accounts Section.")
            print("\t2. To Proceed To Vehicles Section.")
            print("\t3. Exit: To Exit From Admin Section.")
            print()
            # Ask the user for the desired option
            options=input("Enter Your Desired Option: ")

            # choice in accounts section
            if options=="1":
                while True:
                    # Admin choices for accounts section
                    admin_choices_accounts()
                    choice = input("Enter Your Desired Option in Accounts Area. ")
                    if choice == "1":
                            view_all_users_accounts(file_accounts)
                    elif choice == "2":
                        sign_up(accounts_users, user_directory)                
                    elif choice == "3":
                            search_user_account(file_accounts, accounts_users)
                    elif choice == "4":
                            print("Thanks For Using our Services in Admin Accounts Section.")
                            print("Good Bye!!")
                            print()
                            break
                    else:
                        print("Invalid Choice.")
                        print("Please Select From (1/2/3/4)")
                        print()

            # choice in vehicles section
            elif options=="2":
                while True:
                    admin_choices_vehicles()
                    choice = input("Enter Your Desired Option in Vehicles Area. ")
                    if choice == "1":
                            display_car(carfile)
                    elif choice == "2":
                            display_bike(bikefile)
                    elif choice == "3":
                          display_auto(autofile)
                    elif choice == "4":
                            view_all_bookings(booking_file)
                    elif choice == "5":
                        change_membership_status(member_directory, carfile, bikefile, autofile)
                    elif choice == "6":
                            print("Thanks For Using our Services in Admin Vehicles Section.")
                            print("Good Bye!!")
                            print()
                            break
                    else:
                        print("Invalid Choice.")
                        print("Please Select From (1/2/3/4)")
                        print()
            # Exit from admin section
            elif options=="3":
                print("Thanks For Using our Services in Admin Section.")
                print("Good Bye!!")
                print()
                break
            # Invalid choice                            
            else:
                print("Invalid Choice.")
                print("Please Select From (1/2/3)")
                print()
