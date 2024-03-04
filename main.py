from signup import sign_up
from filespaths import file_accounts, accounts_users, user_directory, member_directory, customer_directory, carfile, bikefile, autofile, manual
from login import login
from admin_login import admin_login
from readingpack import manual_redaing

1
# MAIN CHOICE FUNCTION
def main_choice():
    print()
    print("\t\tWELCOME TO RAZA'S TRANSPORTATION SERVICES.")
    print()
    print("\tOnce you are logged in, You have option To proceed as Customer Or Member.")
    print()
    print("\t1.Signup As User.")
    print("\t2.Login As User.")
    print("\t3.Login As Admin.")
    print("\t4.Read Instructions How To use This Program.")
    print("\t5.To Exit From Program.")
    print()
# Main code block
while True:
    main_choice()
    choice=input("Please Enter Your Preferred Option: ")

    if choice=="1":
      
        userfile = sign_up(accounts_users, user_directory)
       

    elif choice=="2":
      
        login(file_accounts, accounts_users, member_directory, customer_directory)
         
    elif choice=="3":
        admin_login( file_accounts, accounts_users, carfile, bikefile, autofile)

    elif choice=="4":
       manual_redaing(manual)

   # Exit from program
    elif choice=="5":
        print("Thanks For Using our Services.")
        print("Good Bye!!")
        print()
        break
    # Invalid choice
    else:
        print("Invalid Choice")
        print("Please Select From (1,2,3,4)")
        print()