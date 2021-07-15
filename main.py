from flight_trip import create_flight, manage_flight_trips, generate_flight_attendees
from passenger import create_passenger, add_passenger
from login import login, register, hash_password


def interface():
    while True:
        log_reg = input("Press 1 to login, press 2 to register, or 0 to exit:  ")
        # Login
        if log_reg == "1":
            username = input("USERNAME:  ")
            password = input("PASSWORD:  ")
            log_in = login(username, password)
            # Check account type
            if log_in == "assistant":
                while True:
                    option = input("OPTIONS \n"
                                   "1 - Create a passenger \n"
                                   "2 - Create a flight \n"
                                   "3 - Add passenger to flight \n"
                                   "4 - Change flight details \n"
                                   "5 - Generate passenger list \n"
                                   "0 - Exit. \n"
                                   "What would you like to do?  ")
                    # 1 - Create Passenger
                    if option == "1":
                        f_name = input("Please input passenger's First Name:  ")
                        l_name = input("Please input passenger's Last Name:  ")
                        passport = input("Please input passenger's Passport Number:  ")
                        age = input("Please input passenger's Age:  ")
                        # Raise error if input is empty
                        try:
                            if not f_name or not l_name or not passport or not age:
                                raise ValueError("Could not create passenger. Please try again.")
                            create_passenger(f_name, l_name, passport, age)
                            print("SUCCESS! PASSENGER CREATED.")
                        except ValueError as err:
                            print(err)

                    # 2 - Create Flight
                    elif option == "2":
                        flight_id = input("Please input flight ID:  ")
                        destination = input("Please input flight Destination:  ")
                        origin = input("Please input flight Origin:  ")
                        vehicle = input("Please input flight Vehicle:  ")
                        duration = input("Please input flight Duration:  ")
                        # Raise error if input is empty
                        try:
                            if not flight_id or not destination or not origin or not vehicle or not duration:
                                raise ValueError("Could not create flight. Please try again.")
                            create_flight(flight_id, destination, origin, vehicle, duration)
                            print("SUCCESS! FLIGHT CREATED.")
                        except ValueError as err:
                            print(err)

                    # 3 - Add Passenger to Flight
                    elif option == "3":
                        passport = input("Please input passenger's Passport Number:  ")
                        flight_id = input("Please input flight ID:  ")
                        try:
                            if not flight_id or not passport:
                                raise ValueError("Could not create flight. Please try again.")
                            add_passenger(flight_id, passport)
                            print(f"SUCCESS! PASSENGER: {passport} ADDED TO FLIGHT: {flight_id}.")
                        except ValueError as err:
                            print(err)

                    # 4 - Change Flight Details
                    elif option == "4":
                        flight_id = input("Please input flight ID:  ")
                        destination = input("Please input NEW flight Destination:  ")
                        origin = input("Please input NEW flight Origin:  ")
                        vehicle = input("Please input NEW flight Vehicle:  ")
                        duration = input("Please input NEW flight Duration:  ")
                        try:
                            if not flight_id or not destination or not origin or not vehicle or not duration:
                                raise ValueError("Could not get flight details. Please try again.")
                            manage_flight_trips(flight_id, destination, origin, vehicle, duration)
                            print(f"SUCCESS! FLIGHT DETAILS CHANGED.")
                        except ValueError as err:
                            print(err)

                    # 5 - Generate Passenger List
                    elif option == "5":
                        generate_flight_attendees()

                    # 0 - Exit interface
                    elif option == "0":
                        print("Thank you. Goodbye!")
                        break

                    # If user inputs wrong code
                    else:
                        print("Sorry something went wrong, please try again.")
            elif log_in == "basic":
                print("You are a basic user.")

        # Register
        elif log_reg == "2":
            username = input("INPUT USERNAME:  ")
            password = input("INPUT PASSWORD:  ")
            hashed_password = hash_password(password)
            first = input("INPUT FIRST NAME:  ")
            last = input("INPUT LAST NAME:  ")
            register(username, hashed_password, first, last)

        elif log_reg == "0":
            print("Thank you. Goodbye!")
            break


interface()
