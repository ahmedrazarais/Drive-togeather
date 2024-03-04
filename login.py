import os    

from filespaths import  carfile, autofile, bikefile
from customer_area import display_available_vehicles, booking_vehicles, display_customer_history,customer_choices
from memberarea import share_car, display_cars, update_vehicle,member_choices,user_choices

accounts_users=[]                     # LIST TO GET ACCOUNTS DATA
account_sep="#@!%^"             # SEPERATOR  




def login(file_accounts, accounts_users,member_directory,customer_directory):
    member=False
    while True:   # taking sername input
        username = input("Enter User Name To Login (enter 0 to return): ")

        if username == "0":    # returning on certain condition
            return

        with open(file_accounts, "r") as accounts:
            accounts_users.clear()  # Clear the list before adding new data
            for line in accounts:
                data = line.strip().split(account_sep)
                user_accounts_dict = {"username": data[0], "password": data[1], "securityanswer": data[2]}
                accounts_users.append(user_accounts_dict)   # update in accountusers list

        found_username = False    # initial it by false
        for check in accounts_users:     # apply loop on 2d data form
            if username == check["username"]:   # Checking if username present in list
                found_username = True    # if found then make it true

                # Now taking input Of Password
                while True:
                    pswd = input("Enter Your Password For Login (enter 0 to return): ")
                    if pswd == "0":  # returning on certain condition
                        return

                    # Checking if password presnt in dictionary
                    if pswd == check["password"]:
                        print("Login Successfully!!")
                        print()    
                    # after suceessfull login make 2 file for member and customer but for one time
                        member_file = os.path.join(member_directory, f"{username}.txt")                       
                        customer_file = os.path.join(customer_directory, f"{username}.txt")

                        if not os.path.exists(member_file):
                            with open(member_file, "w"):
                                pass

                        # Create the customer file if it doesn't exist
                        if not os.path.exists(customer_file):
                            with open(customer_file, "w"):
                                pass

                        
                      

                        file_name = ""  # Assign a default value to file_name

                       # apply loop for user choice

                        while True:
                            user_choices()
                            # This is choice to act as member or customer
                            choice=input("Enter Your Desired Options :")

                            # If he want to act as member
                            if choice=="1":
                                # if user select to proceed as member so first open his file check if he is member then proceed
                                with open(member_file,"r") as file:
                                    lines=file.readlines()
                                    for line in lines:
                                        data=line.strip().split("#")
                                    for i in data:
                                        if i =="OFF":
                                            member=True                               
                                    if not member:
                                        while True:
                                            member_choices()

                                            choice=input("Select Your Choice In Member Section :")
                                            if choice=="1":              
                                                # Pass file_name as a parameter
                                              file_name = share_car(file_name, member_file, customer_file)


                                            elif choice=="2":
                                                display_cars(member_file)
                                            

                                            elif choice=="3":
                                                update_vehicle(member_file,carfile, bikefile, autofile)


                                            elif choice=="4":
                                                print("Thanks For Using our Services.")
                                                print("Good Bye!!")
                                                print()
                                                break
                                            else:
                                                print("Invalid Choice.")
                                                print("Please Select From (1/2/3/4)")
                                                print()
                                    else:
                                        print("Oops! Your Membership Is Cancel By Admin. You Can't Access Our Services.")
                                        print()
                                        return


                           # If he want to act as customer
                            elif choice=="2": 
                              while True:
                                customer_choices()
                                choice=input("Select Your Choice In Customer Section :")
                                if choice=="1":
                                    display_available_vehicles(carfile, bikefile, autofile)
                                elif choice=="2":
                                    booking_vehicles(carfile,bikefile,autofile,customer_file)
                                elif choice=="3":
                                    display_customer_history(customer_file)
                                elif choice=="4":
                                    print("Thanks For Using our Services.")
                                    print("Good Bye!!")
                                    print()
                                    break
                                else:
                                    print("Invalid Choice.")
                                    print("Please Select From (1/2/3/4)")
                                    print()          
                              
                          # if user want to exit
                            elif choice=="3":
                                print("Thanks For Using our Services.")
                                print("Good Bye!!")
                                print()
                                break

                            else:
                                print("Invalid Choice.")
                                print("Please Select From (1/2/3)")
                                print()
                    
                        return    # After Successfull Login
                    

                    # if password not match
                    else:
                        print("Incorrect Password")
                        print()
                        print("Answer The Security Question And Get Access To Reset Password")
                        print()
                        # Asking security question
                        security_ans_check = input("What Is Your Favorite Pet Animal?: ")
                        # Checking if answer match with dictionary value
                        if security_ans_check == check["securityanswer"]:
                            print("Alright, Now reset Your password")
                            print()

                            # If Security answer match
                            while True:
                                new_pswd = input("Enter New Password: ").strip()
                                # Apply condition for password strength
                                if len(new_pswd) >= 8 and any(char.isdigit() for char in new_pswd) and any(
                                        char.isalpha() for char in new_pswd):
                                    print("Strong password")
                                elif len(new_pswd) >= 6:
                                    print("Moderate password")
                                else:
                                    print("Weak password, password length should be minimum 6 characters.")
                                # Ask user if they want to improve their password
                                while True:
                                    ask_for_better = input("Do you want to make it better? (Y/N): ").lower()
                                    if ask_for_better in ["n", "y"]:
                                        break
                                    else:
                                        print("Please select 'Y' or 'N'.")
                                if ask_for_better == "n":
                                    break
                                
                            # Update Dictionary key With New Password
                            check["password"] = new_pswd  # Update password
                            
                            # Now Writting New Data With Upadte 
                            with open(file_accounts, "w") as accounts:
                                for account in accounts_users:
                                    accounts.write(
                                        f"{account['username']}{account_sep}{account['password']}{account_sep}{account['securityanswer']}\n")
                            print("Password updated successfully!")
                            print()
                            return    # After successfull login return from function
                        else:     # If security Answer Not matches
                            print("Access Denied..")
                            print()
                            return      # Return as just give one chance to answer 
        if not found_username:        # If username is not correct
            print()
            print("Incorrect Username")
            print()