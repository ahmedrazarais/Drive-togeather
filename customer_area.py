from filespaths import member_directory,booking_file
from memberarea import update_member_files



# function to display customer choices
def customer_choices():
    print()
    print("\t\tWelcome To Customer Section")
    print("\t1.View All Vehicles Available For Booking.")
    print("\t2.Book A Vehicle.")
    print("\t3.View Your Previous Bookings History.")
    print("\t4.Exit: To Exit From Customer Secion.")
    print()

# make a function to display available vehicles for booking to custome first ask for category also check one thing only show that vehicles which are active
def display_available_vehicles(carfile, bikefile, autofile):
    # Ask customer to select vehicle category
    while True:
        print()
        print("\tSelect Your Vehicle Category")
        print("\t1. Select 1 To View Available Cars For Booking.")
        print("\t2. Select 2 To View Available Bikes For Booking.")
        print("\t3. Select 3 To View Available Automobiles For Booking.")
        print("\t4. Select 4 To Go Back.")
        print()
        vehicle_category = input("Enter Your Desired Option: ")
        if vehicle_category == "4":    # Go back
            return
        print()

        # Check if the input is valid
        if vehicle_category in ["1", "2", "3"]:
            break
        else:
            print("Invalid Choice.")
            print("Please Select From (1/2/3)")
            print()
    # Display available vehicles based on the category
    if vehicle_category == "1":
        display_car(carfile)
   
    elif vehicle_category == "2":
        display_bike(bikefile)
        

    elif vehicle_category == "3":
        display_auto(autofile)
       
# function to display cars
def display_car(carfile):
    try:    # opening the file
            with open(carfile, "r") as file:
                lines = file.readlines()
                if not lines:  # Check if the file is empty
                    print()
                    print("No cars available for booking.")
                    print()
                else:
                    print()
                    print("\tHere Are The Available Cars For Booking.")
                    print()
                    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Vehicle Name", "Model", "Owner Name", "Rent Price","Status"))
                    print("="*100)  # Separator line
                    for line in lines:
                        # Split the line into parts
                        parts = line.strip().split("#")
                        if len(parts) >= 6:  # Check if there are at least 6 parts
                            id, vehicle_name, model, owner_name, rent_price,status = parts[:6]  # Take only the first six parts
                            # only show active vehicles
                            if status=="ACTIVE":
                                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format(id, vehicle_name, model, owner_name, rent_price,status))
                        else:
                            print(f"Invalid data format: {line.strip()}")  # Print error message for invalid data
    except FileNotFoundError:
            print("Car file not found.")


# function to display bikes
def display_bike(bikefile):
    try:
            with open(bikefile, "r") as file:
                lines = file.readlines()
                if not lines:  # Check if the file is empty
                    print()
                    print("No bikes available for booking.")
                    print()
                else:
                    print()
                    print("\tHere Are The Available Bikes For Booking.")
                    print()
                    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Vehicle Name", "Model", "Owner Name", "Rent Price","Status"))
                    print("="*100)  # Separator line
                    for line in lines:
                        # Split the line into parts
                        parts = line.strip().split("#")
                        if len(parts) >= 6:
                            id, vehicle_name, model, owner_name, rent_price,status = parts[:6]
                            # only show active vehicles
                            if status=="ACTIVE":
                                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format(id, vehicle_name, model, owner_name, rent_price,status))
                        else:
                            print(f"Invalid data format: {line.strip()}")
    except FileNotFoundError:
            print("Bike file not found.")

# function to display automobiles
def display_auto(autofile):
     try:
            with open(autofile, "r") as file:
                lines = file.readlines()
                if not lines:  # Check if the file is empty
                    print()
                    print("No automobiles available for booking.")
                    print()
                else:
                    print()
                    print("\tHere Are The Available Automobiles For Booking.")
                    print()
                    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Vehicle Name", "Model", "Owner Name", "Rent Price","Status"))
                    print("="*100)  # Separator line
                    for line in lines:
                        # Split the line into parts
                        parts = line.strip().split("#")
                        if len(parts) >= 6:
                            id, vehicle_name, model, owner_name, rent_price,status = parts[:6]

                            # only show active vehicles
                            if status=="ACTIVE":
                                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format(id, vehicle_name, model, owner_name, rent_price,status))
                        else:
                            print(f"Invalid data format: {line.strip()}")
     except FileNotFoundError:
            print("Automobile file not found.")

# function to book a vehicle
def booking_vehicles(carfile,bikefile,autofile,customer_file):
    while True:
        print()
        print("\tSelect Your Vehicle Category")
        print("\t1. Select 1 To Book A Car.")
        print("\t2. Select 2 To Book A Bike.")
        print("\t3. Select 3 To Book An Automobile.")
        print("\t4. Select 4 To Go Back.")
        print()
        vehicle_category = input("Enter Your Desired Option: ")
        if vehicle_category == "4":
            return
        print()
        if vehicle_category in ["1", "2", "3"]:
            break
        else:
            print("Invalid Choice.")
            print("Please Select From (1/2/3)")
            print()
    # Display available vehicles based on the category
    if vehicle_category == "1":
        display_car(carfile)
        book_car(carfile,customer_file, booking_file)
    elif vehicle_category == "2":
        display_bike(bikefile)
        book_bike(bikefile,customer_file,booking_file)
       
    elif vehicle_category == "3":
        display_auto(autofile)
        book_auto(autofile,customer_file,booking_file)


# function to book a car
def book_car(carfile, customer_file, booking_file):
    import time   # import time to write in customer file the time of booking
    
    # Check if there is data in the carfile and if any car has an active status
    with open(carfile, "r") as file:
        lines = file.readlines()
        active_car_found = False
        for line in lines:
            parts = line.strip().split("#")
            if len(parts) >= 6 and parts[5] == "ACTIVE":
                active_car_found = True
                break
    # If there are no cars or no active cars, return
    if not lines or not active_car_found:
        print("No cars available for booking.")
        return

    # If there are active cars, proceed with booking
    time_now = time.ctime()
    while True:
        try:
            # Ask the user for the car ID to book
            vehicle_id = int(input("Enter the ID of the car to book (enter 0 to go back): "))
            if vehicle_id == 0:
                return
            found = False      # initialize found to False

            # open the carfile and read the lines
            with open(carfile, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split("#")
                    if len(parts) >= 6:
                        id, vehicle_name, model, owner_name, rent_price, status = parts[:6]

                        # Check if the car ID is found and the car is active
                        if int(id) == vehicle_id and status == "ACTIVE":
                            found = True

                            # if id is found then ask for the number of days to book the car
                            while True:
                                try:
                                    days = int(input("Enter the number of days to book the car: "))
                                    if days > 0:
                                        print()
                                        print(f"Car Booked Successfully for {days} days!")

                                        # calculate the total rent to pay
                                        fair = int(rent_price) * days
                                        print()
                                        break
                                    else:
                                        print("Days should be greater than 0.")
                                        print()
                                except ValueError:
                                    print("Days should be a number.")
                                    print()
                            # Record booking details in customer file
                            with open(customer_file, "a+") as file:
                                file.write(f"Recorded Time: {time_now}\n")  
                                file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                                file.write("\n\n")
                            # Update car status to non-active after booking
                            with open(carfile, "r") as file:
                                lines = file.readlines()
                            for line in lines:
                                parts = line.strip().split("#")
                                if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                    parts[5] = "NONACTIVE"
                                    lines[lines.index(line)] = "#".join(parts) + "\n"
                            with open(carfile, "w") as file:
                                file.writelines(lines)
                            # Record booking details in booking file
                            with open(booking_file, "a+") as file:
                                file.write(f"Recorded Time: {time_now}\n")  
                                file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                                file.write("\n\n")
                            print("Car Booked Successfully. Check Your Booking History For Details.")
                            print("Enjoy Your Ride!!")
                            print()
                            update_member_files(member_directory, vehicle_id, status)
                            return 

            # If the car ID is not found or the car is not active, print an error message
            if not found:
                print("Car ID not found or car is not available for booking. Please write a correct ID.")
                print() 
        except ValueError:
            print("ID should be a number.")
            print()


def book_bike(bikefile, customer_file, booking_file):
    import time
    
    # Check if there is data in the bikefile and if any bike has an active status
    with open(bikefile, "r") as file:
        lines = file.readlines()
        active_bike_found = False
        for line in lines:
            parts = line.strip().split("#")
            if len(parts) >= 6 and parts[5] == "ACTIVE":
                active_bike_found = True
                break
    
    if not lines or not active_bike_found:
        print("No bikes available for booking.")
        return

    # If there are active bikes, proceed with booking
    time_now = time.ctime()
    while True:
        try:
            vehicle_id = int(input("Enter the ID of the bike to book (enter 0 to go back): "))
            if vehicle_id == 0:
                return
            found = False
            with open(bikefile, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split("#")
                    if len(parts) >= 6:
                        id, vehicle_name, model, owner_name, rent_price, status = parts[:6]
                        if int(id) == vehicle_id and status == "ACTIVE":
                            found = True
                            while True:
                                try:
                                    days = int(input("Enter the number of days to book the bike: "))
                                    if days > 0:
                                        print()
                                        print(f"Bike Booked Successfully for {days} days!")
                                        fair = int(rent_price) * days
                                        print()
                                        break
                                    else:
                                        print("Days should be greater than 0.")
                                        print()
                                except ValueError:
                                    print("Days should be a number.")
                                    print()
                            # Record booking details in customer file
                            with open(customer_file, "a+") as file:
                                file.write(f"Recorded Time: {time_now}\n")  
                                file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                                file.write("\n\n")
                            # Update bike status to non-active after booking
                            with open(bikefile, "r") as file:
                                lines = file.readlines()
                            for line in lines:
                                parts = line.strip().split("#")
                                if len(parts) >= 6 and int(parts[0]) == vehicle_id:
                                    parts[5] = "NONACTIVE"
                           
                                    lines[lines.index(line)] = "#".join(parts) + "\n"
                            with open(bikefile, "w") as file:
                                file.writelines(lines)
                            # Record booking details in booking file
                            with open(booking_file, "a+") as file:
                                file.write(f"Recorded Time: {time_now}\n")  
                                file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                                file.write("\n\n")
                            print("Bike Booked Successfully. Check Your Booking History For Details.")
                            print("Enjoy Your Ride!!")
                            update_member_files(member_directory, vehicle_id, status)
                            print()
                            return 
            if not found:
                print("Bike ID not found or bike is not available for booking. Please write a correct ID.")
                print() 
        except ValueError:
            print("ID should be a number.")
            print()

def book_auto(autofile, customer_file, booking_file):
    import time

    # Check if there is data in the autofile and if any auto has an active status
    with open(autofile, "r") as file:
        lines = file.readlines()
        active_auto_found = any(line.strip().split("#")[5] == "ACTIVE" for line in lines)

    if not lines or not active_auto_found:
        print("No autos available for booking.")
        return

    # If there are active autos, proceed with booking
    time_now = time.ctime()
    while True:
        try:
            vehicle_id = int(input("Enter the ID of the auto to book (enter 0 to go back): "))
            if vehicle_id == 0:
                return

            found = False
            with open(autofile, "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split("#")
                if len(parts) >= 6:
                    id, vehicle_name, model, owner_name, rent_price, status = parts[:6]
                    if int(id) == vehicle_id and status == "ACTIVE":
                        found = True
                        while True:
                            try:
                                days = int(input("Enter the number of days to book the auto: "))
                                if days > 0:
                                    print()
                                    print(f"Auto Booked Successfully for {days} days!")
                                    fair = int(rent_price) * days
                                    print()
                                    break
                                else:
                                    print("Days should be greater than 0.")
                                    print()
                            except ValueError:
                                print("Days should be a number.")
                                print()

            if found:
                time_now = time.ctime()
                with open(customer_file, "a+") as file:
                    file.write(f"Recorded Time: {time_now}\n")  
                    file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                    file.write("\n\n")

                with open(autofile, "r") as file:
                    lines = file.readlines()

                for line in lines:
                    parts = line.strip().split("#")
                    if len(parts) >= 6:
                        id, vehicle_name, model, owner_name, rent_price, status = parts[:6]
                        if int(id) == vehicle_id:
                            parts[5] = "NONACTIVE"
                       
                            lines[lines.index(line)] = "#".join(parts) + "\n"

                with open(autofile, "w") as file:
                    file.writelines(lines)

                with open(booking_file, "a+") as file:
                    file.write(f"Recorded Time: {time_now}\n")  
                    file.write(f"Vehicle Id: {vehicle_id}\nVehicle Name: {vehicle_name}\nVehicle Model: {model}\nOwner Name: {owner_name}\nTotal Days: {days}\nTotal Rent To Pay: {fair}\n")
                    file.write("\n\n")

                print("Auto Booked Successfully. Check Your Booking History For Details.")
                print("Enjoy Your Ride!!")
                print()
                update_member_files(member_directory, vehicle_id, status)
                return 
            if not found:
                print("Auto ID not found or auto is not available for booking. Please write a correct ID.")
                print() 
        except ValueError:
            print("ID should be a number.")
            print()




# function to display customer history
def display_customer_history(customer_file):
    with open(customer_file) as file:
       lines= file.read()
       if not lines:   # if no history found
           print()
           print("You come so early!! No history found.")
           print("Book Some Rides First.Then Comeback To Check History.")
       else:
           print("\t\tHere Is Your Booking History.")
           print()
           print(lines)
           print()