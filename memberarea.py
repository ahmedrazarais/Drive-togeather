import random
import os
from filespaths import idfile,carfile,autofile,bikefile


def user_choices():
    print()
    print("\t\tWelcome To Ride-Share-Link")
    print("\t1.Proceed As A Member.")
    print("\t2.Proceed As A Customer.")
    print("\t3.Exit: To Exit From Program.")  
    print()


# Work if proceed as a member
def member_choices():
    print()
    print("\t\tWelcome TO Member Section")
    print("\t1.Share Your Vehicles For Booking.")
    print("\t2.View All Your Vehicles That You set for Booking.")
    print("\t3.Update Your Vehicles Information.")
    print("\t4.Exit: To Exit From Program.")
    print()

#  making function to provide user what he ca update in information


def update_choices():
    print()
    print("\t\tWelcome TO Update Section")
    print("\t1.Update Your Vehicle Name.")
    print("\t2.Update Your Vehicle Model.")
    print("\t3.Update Your Rent Price.")
    print("\t4.update Your Status.")
    print()
def display_cars(member_file):
    try:
        with open(member_file, "r") as file:
            lines = file.readlines()
            if not lines:  # Check if the file is empty
                print()
                print("No cars set for booking.")
                print("Please set your cars for booking.")
                print()
            else:
                print()
                print("\tHere Are Your Vehicles That You Set For Booking.")
                print()
                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Vehicle Name", "Model", "Owner Name", "Rent Price","Status","Vehicle Status"))
                print("="*100)  # Separator line
                for line in lines:
                    # Split the line into parts
                    parts = line.strip().split("#")
                    if len(parts) >= 6:  # Check if there are at least 6 parts
                        id, vehicle_name, model, owner_name, rent_price,status,vehicle_status = parts[:7]  # Take only the first six parts
                        print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format(id, vehicle_name, model, owner_name, rent_price,status,vehicle_status))
                    else:
                        print(f"Invalid data format: {line.strip()}")  # Print error message for invalid data
    except FileNotFoundError:
        print("Member file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Function to share a vehicle
def share_car(file_name, member_file, customer_file):
    global used_ids  # Use the global variable

    print("\tHere You Can Share Your Car For Booking.")
    print("\tPlease Fill The Following Details.")
    print()

    # Prompt user to select vehicle category
    while True:
        print()
        print("\tSelect Your Vehicle Category")
        print("\t1. Select 1 To Share Your Car For Booking.")
        print("\t2. Select 2 To Share Your Bike For Booking.")
        print("\t3. Select 3 To Share Your Automobile For Booking.")
        print("\t4. Select 4 To Go Back.")
        print()
        vehicle_category = input("Enter Your Desired Option: ")
        if vehicle_category == "4":
            return file_name, member_file, customer_file
        print()
        if vehicle_category in ["1", "2", "3"]:
            break
        else:
            print("Invalid Choice.")
            print("Please Select From (1/2/3)")
            print()

    # Prompt user for vehicle details
    while True:
        vehicle_name = input("Enter Your Vehicle Name (enter 0 to go back): ")
        print()
        if vehicle_name == "0":
            return file_name, member_file, customer_file
        if vehicle_name != "":
            break
        else:
            print()
            print("Vehicle Name is Mandatory.")
            print()

    while True:
        vehicle_model = input("Enter Your Vehicle Model (enter 0 to go back): ")
        print()
        if vehicle_model == "0":
            return file_name, member_file, customer_file
        if vehicle_model != "":
            break
        else:
            print()
            print("Oops!!Vehicle Model is Mandatory.")
            print()

    while True:
        owner_name = input("Enter Owner Name (enter 0 to go back): ")
        print()
        if owner_name == "0":
            return file_name, member_file, customer_file
        if owner_name != "" and owner_name.isalpha():
            break
        else:
            print()
            print("Name is Mandatory. Only Alphabets are allowed.")
            print()

    while True:
        try:
            vehicle_price = int(input("Enter Rent Price For Booking (enter 0 to go back): "))
            print()
            if vehicle_price == 0:
                return file_name, member_file, customer_file
            if vehicle_price != "" and vehicle_price > 0:
                break
            else:
                print()
                print("Price is Mandatory To Set Your Vehicle For Booking.Must Be Greater Than 0.")
                print()
        except ValueError:
            print("Price Should be in Digits.")
            print()

    while True:
        status = input("Share your  Vehicle status active or not active: ").strip().upper()
        print()
        if status in ["ACTIVE", "NONACTIVE"]:
            break
        else:
            print("Invalid Choice.")
            print("Please Select From (Active/Nonactive)")
            print()

    # Determine the file to write based on vehicle category
    if vehicle_category == "1":
        file_name = carfile
    elif vehicle_category == "2":
        file_name = bikefile
    elif vehicle_category == "3":
        file_name = autofile

    # Assign a unique ID to the vehicle
    # check in filename member file id must not there  also id assign to one user not repeated for another user
    # make a file to store all ids and check id not repeated.
    with open(idfile, "r") as file:
        used_ids = file.read()
        used_ids = used_ids.split("\n")
        while True:
            vehicle_id = random.randint(1000, 9999)
            if str(vehicle_id) not in used_ids:
                used_ids.append(str(vehicle_id))
                with open(idfile, "a") as file:
                    file.write(f"{vehicle_id}\n")
                break
    vehicle_status="Not-Booked"   # if not booked by any customer
    membership="Member"   # if user is member
    # Write vehicle details to the appropriate files
    with open(member_file, "a+") as file:
        file.write(f"{vehicle_id}#{vehicle_name}#{vehicle_model}#{owner_name}#{vehicle_price}#{status}#{vehicle_status}#{membership}\n")

    with open(file_name, "a+") as file:
        file.write(f"{vehicle_id}#{vehicle_name}#{vehicle_model}#{owner_name}#{vehicle_price}#{status}\n")

    print()
    print("Congratulations!! Your Vehicle is Set For Booking.")
    print("Thanks For Sharing Your Vehicle.")
    print("we will notify you when someone book your vehicle.")
    print()

    # Return the file_name for further use
    return file_name, member_file, customer_file
# # Main code block


 
# Function to update vehicle information
def update_vehicle(member_file, carfile, bikefile, autofile):
    # call display_cars function to show member his contributed cars
    display_cars(member_file)
    
    # Ask member to enter the ID of the vehicle to update and check if id match with file
    while True:
        try:
            with open(member_file, "r") as file:
                lines = file.readlines()
                if not lines:  # Check if the file is empty
                    print()
                    print("Oops!! No cars information Recieved Yet To Update.")
                    print()
                    return
                else:
                    print()
                    print()
                    vehicle_id = int(input("Enter the ID of the vehicle to update (enter 0 to go back): "))
                    if vehicle_id == 0:
                        return
                    
                    # open the member file to read the data
                    with open(member_file, "r") as file:
                        lines = file.readlines()
                    found = False
                    # chheck if id matches or not.
                    for line in lines:
                        parts = line.strip().split("#")
                        if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                            found = True
                            while True:
                                update_choices()
                                choice = input("Enter Your Desired Option In Update Area ")
                                # provide user to update his vehicle information
                                # write updated thing in his file as well as in main file car bike or auto
                                if choice == "1":
                                    print()
                                    display_cars(member_file)
                                    print(f"You Can Now Update Vehicle Name For ID {vehicle_id}.")
                                    print()
                                    vehicle_name = input("Enter the updated vehicle name (enter 0 To Back)").strip()
                                    if vehicle_name == "0":
                                        return
                                    if vehicle_name != "":
                                        parts[1] = vehicle_name
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(member_file, "w") as file:
                                            file.writelines(lines)
            
                                        with open(carfile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[1] = vehicle_name
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(carfile, "w") as file:
                                            file.writelines(lines)
                                        with open(bikefile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[1] = vehicle_name
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(bikefile, "w") as file:
                                            file.writelines(lines)
                                        with open(autofile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[1] = vehicle_name
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(autofile, "w") as file:
                                            file.writelines(lines)
                                        print("Vehicle name updated successfully.")
                                        print()
                                        display_cars(member_file)
                                        print()
                                        break
                                    else:
                                        print("Vehicle name is mandatory.")
                                        print()
                                elif choice == "2":
                                    print()
                                    display_cars(member_file)
                                    print(f"You Can Now Update Vehicle Model For ID {vehicle_id}.")
                                    print()
                                    vehicle_model = input("Enter the updated vehicle model (enter 0 To Back): ").strip()
                                    if vehicle_model == "0":
                                        return
                                    if vehicle_model != "":
                                        parts[2] = vehicle_model
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(member_file, "w") as file:
                                            file.writelines(lines)
                                            
                                        with open(carfile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[2] = vehicle_model
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(carfile, "w") as file:
                                            file.writelines(lines)
                                        with open(bikefile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[2] = vehicle_model
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(bikefile, "w") as file:
                                            file.writelines(lines)
                                        with open(autofile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[2] = vehicle_model
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(autofile, "w") as file:
                                            file.writelines(lines)
                                        print("Vehicle model updated successfully.")
                                        print()
                                        display_cars(member_file)
                                        break
                                    else:
                                        print("Vehicle model is mandatory.")
                                        print()
                                elif choice == "3":
                                    while True:
                                        try:
                                            print()
                                            display_cars(member_file)
                                            print(f"You Can Now Update Vehicle Price For ID {vehicle_id}.")
                                            print()
                                            vehicle_price = int(input("Enter the updated rent price (enter 0 To Back): "))
                                            if vehicle_price == 0:
                                                return
                                            if vehicle_price > 0:
                                                parts[4] = str(vehicle_price)
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                                with open(member_file, "w") as file:
                                                    file.writelines(lines)
                                                    # call display member file
                                               

                                                with open(carfile, "r") as file:
                                                    lines = file.readlines()
                                                for line in lines:
                                                    parts = line.strip().split("#")
                                                    if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                        parts[4] = str(vehicle_price)
                                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                                with open(carfile, "w") as file:
                                                    file.writelines(lines)
                                                with open(bikefile, "r") as file:
                                                    lines = file.readlines()
                                                for line in lines:
                                                    parts = line.strip().split("#")
                                                    if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                        parts[4] = str(vehicle_price)
                                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                                with open(bikefile, "w") as file:
                                                    file.writelines(lines)
                                                with open(autofile, "r") as file:
                                                    lines = file.readlines()
                                                for line in lines:
                                                    parts = line.strip().split("#")
                                                    if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                        parts[4] = str(vehicle_price)
                                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                                with open(autofile, "w") as file:
                                                    file.writelines(lines)
                                                print("Rent price updated successfully.")
                                                print()
                                                display_cars(member_file)
                                                break
                                            else:
                                                print("Rent price should be greater than 0.")
                                                print()
                                        except ValueError:
                                            print("Rent price should be in digits.")
                                            print()
                                    break
                                elif choice == "4":
                                    print()
                                    display_cars(member_file)
                                    print(f"You Can Now Update Vehicle Status For ID {vehicle_id}.")
                                    print()
                                    status = input("Enter the updated status (active/nonactive): ").strip().upper()
                                    if status in ["ACTIVE", "NONACTIVE"]:
                                        parts[5] = status
                                        lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(member_file, "w") as file:
                                            file.writelines(lines)
                                          
                                        with open(carfile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[5] = status
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(carfile, "w") as file:
                                            file.writelines(lines)
                                        with open(bikefile, "r") as file:
                                            lines = file.readlines()
                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[5] = status
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                        with open(bikefile, "w") as file:
                                            file.writelines(lines)

                                        with open(autofile, "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            parts = line.strip().split("#")
                                            if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                                parts[5] = status
                                                lines[lines.index(line)] = "#".join(parts) + "\n"
                                                
                                        with open(autofile, "w") as file:
                                            file.writelines(lines)
                                        print("Status updated successfully.")
                                        print()
                                        display_cars(member_file)
                                        break
                                    else:
                                        print("Invalid status.")
                                        print()
                               


                                
                              

                                else:
                                    print("Invalid Choice.")
                                    print("Please Select From (1/2/3/4/5)")
                                    print()
                            break

                    if not found:
                        print("Vehicle ID not found.")
                        print()
        except ValueError:
            print("ID should be a number.")
            print()


def update_member_files(member_directory, vehicle_id, status):
    # List all files in the member directory
    files = os.listdir(member_directory)
    
    # Iterate through each file
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(member_directory, file_name)
            # Open the file for reading and writing
            with open(file_path, 'r+') as file:
                lines = file.readlines()
                modified = False
                # Iterate through each line in the file
                for index, line in enumerate(lines):
                    # Check if the vehicle ID is present in the line
                    if str(vehicle_id) in line:
                        # If found, replace the status with the new status
                        parts = line.strip().split("#")
                        if len(parts) >= 7 and parts[6].strip() == "Not-Booked":
                            parts[6] = "Booked"
                            lines[index] = "#".join(parts) + "\n"
                            modified = True
                # If the file was modified, write the changes back to the file
                if modified:
                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()