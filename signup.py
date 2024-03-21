from filespaths import file_accounts,account_sep,user_directory
import os
def sign_up(accounts_users,userfile):
    with open(file_accounts,"a+") as accounts:
                accounts.seek(0)      # seek cursor to zero
                # applying loop for taking linewise enteries
                for line in accounts:
                    # making each line in file a list
                    # using hardcode seperator
                    data=line.strip().split(f"{account_sep}")
                    # now appending in dictionary every user details 
                    user_accounts_dict={"username":data[0],"password":data[1],"securityanswer":data[2]}
                    #appending all dictionaries in list
                    accounts_users.append(user_accounts_dict) 
    while True:
     user_name=input("Enter Your UserName (enter 0 to return back):").strip()   # removing left empty spaces

    # Apply condition for exit from function
     if user_name == "0":
        return   # if user enter 0 then return from function
    
    # checking that user name should contain something not empty
     if user_name != "": 
                duplicate=False  
                for check in accounts_users:
                        # if username exist in file
                    if  user_name.lower() == check["username"].lower() :
                            print("Sorry This Username is already taken")
                            print()
                            duplicate=True
                            break                  
                if not duplicate:                       
                  while True:
                        pswd = input("Enter Strong Password:").strip()
                        if len(pswd) >= 8 and any(char.isdigit() for char in pswd) and any(
                                        char.isalpha() for char in pswd):
                                    print("Strong password")
                        elif len(pswd) >= 6:
                                    print("Moderate password")
                        else:
                                    print("Weak password, password length should be minimum 6 characters.")
                       
                        #   # asking user if he wants to do password more better
                        while True:
                           ask_for_better = input("Do you want to make it better? (Y/N):").lower()
                           if ask_for_better in ["n", "y"]:
                             break
                           else:
                            print("Please select 'Y' or 'N'.")
                         # if he dont want to make it better than
                        if ask_for_better == "n":
                            print("Alright Your Password Is set")
                            break
                  while True:     # Asking Security question BY user
                        security_ques=input("What is Your favourite pet animal?:")

                        if security_ques!="":   # checking for not empty
                         break

                        else:
                            print("Must answer This question for security purpose")
                            print()
                  print()
                  print("Signup Successfull")
                  print()
                                
                  # After successfull signup make file of users
                  user_file = os.path.join(user_directory, f"{user_name}.txt")
                  with open(user_file, "w"):
                    pass
                
                # writting all three things in file
                  with open (file_accounts,"a+") as accounts:
                   accounts.write(f"{user_name}{account_sep}{pswd}{account_sep}{security_ques}\n")
                   accounts.seek(0) # seek to zero after writting                
                    # breaking after all operations
                  return userfile      # returning userfiles

     else:
        print("Username is Mandatory For Signup")
        print()

