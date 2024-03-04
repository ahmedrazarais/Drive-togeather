import os
# Description: This file contains the functions for the admin to view all the vehicles available for booking, view all the booked vehicles, and change the membership status of any user.



# Display all cars available for booking
def view_all_bookings(booking_file):
   #  try to open the file
   with open(booking_file) as file:
         lines= file.read()
         # if file is empty
         if not lines:
              print()
              print("No booking history found.")
              print("Book Some Rides First.Then Comeback To Check History.")
              print()
            # if file is not empty
         else:
              print("\t\tHere Is The Booking History.")
              print()
              # print the file content
              print(lines)
              print()





# Change the membership status of any user
def change_membership_status(member_directory,carfile,bikefile,autofile):
    update=[]
    while True:
        # ask the user for the username to change membership status
        input_username = input("Enter the username of the user to change membership status (enter 0 to back): ")
        if input_username == "0":   # if user enter 0 then
            return   # return from function

        # check if the file exists
        file_path = os.path.join(member_directory, input_username + ".txt")
        if os.path.exists(file_path):
            # if file exists then open the file and change the membership status
            try:
                with open(file_path, "r") as file:
                    lines = file.readlines()
                if lines:   # if file is not empty
                    updated_lines = []
                    membership_status_changed = False
                    for line in lines:
                        parts = line.strip().split("#")
                        if len(parts) >= 7 :
                            # if membership status is member then change it to OFF
                            if parts[-1] == "Member":
                                parts[-1] = "OFF"
                                parts[-3]="NONACTIVE"    # also change the status of car, bike, auto to nonactive


                                membership_status_changed = True
                            updated_lines.append("#".join(parts) + "\n")
                        
                        # if membership status is already OFF then no need to change
                        else:
                            updated_lines.append(line)
                    # if membership status changed then write the updated lines in the file
                    if membership_status_changed:
                        with open(file_path, "w") as file:
                            file.writelines(updated_lines)
                            print("Membership status changed successfully!")
                        # when status changed then open the  file and append its id in list.
                        with open(file_path, "r") as file:
                            lines=file.readlines()
                            for line in lines:
                                parts=line.strip().split("#")
                                if len(parts)>=7:
                                    id=parts[0]
                                    update.append(id)
                        # when id get in update list now check in all 3 files carfile bikefile auto file check where these ids found change then status to nonactive
                        with open(carfile, "r") as file:
                            lines = file.readlines()
                            for line in lines:
                                parts = line.strip().split("#")
                                if len(parts) >= 6:
                                    if parts[0] in update:
                                        parts[5] = "NONACTIVE"
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(carfile, "w") as file:
                                            file.writelines(lines)

                        with open(bikefile, "r") as file:
                            lines = file.readlines()
                            for line in lines:
                                parts = line.strip().split("#")
                                if len(parts) >= 6:
                                    if parts[0] in update:
                                        parts[5] = "NONACTIVE"
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(bikefile, "w") as file:
                                            file.writelines(lines)

                        with open(autofile, "r") as file:
                            lines = file.readlines()
                            for line in lines:
                                parts = line.strip().split("#")
                                if len(parts) >= 6:
                                    if parts[0] in update:
                                        parts[5] = "NONACTIVE"
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(autofile, "w") as file:
                                            file.writelines(lines)
                    else:
                        print("No change required. Membership status was not Member.")
                    print()
                else:
                    with open(file_path,"a+") as file:
                        file.write(f"{"Nothing"}#{"OFF"}")
                    print("Membership status changed successfully!")
                    print()
            except FileNotFoundError:
                print(f"No user information found with username {input_username}.")
                print()
        # if file does not exist then print an error message
        else:
            print(f"No user information found with username {input_username}.")
            print()






# making choices for admin in vehicles section
def admin_choices_vehicles():
    print("\t\tWelcome To Admin Vehicles Section")
    print("\t1.View All Cars Available For Booking.")
    print("\t2.View All Bikes Available For Booking.")
    print("\t3.View All Automobiles Available For Booking.")
    print("\t4.View All Booked Cars.")
    print("\t5.Change Membership Status Of Any User.")
    print("\t6.Exit: To Exit From Vehicles Section.")
    print()
