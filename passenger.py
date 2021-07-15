
import json


# Creates a passenger and adds passenger info to database
def create_passenger(first_name, last_name, passport_number, age,):
    new_passenger = {'passport': passport_number,
                     'first_name': first_name.lower(),
                     'last_name': last_name.lower(),
                     'age': age}

    # Reads, Updates and Closes json file
    try:
        with open("passengers.json", "r+") as read_file:
            data = json.load(read_file)
            data["passenger"].append(new_passenger)
            read_file.seek(0)
            json.dump(data, read_file, indent=4)
    except FileNotFoundError as err:
        return "File not found"


# Add passenger to flight trip
def add_passenger(flight_id, passport):
    # Get passenger info from passenger.json
    try:
        with open("passengers.json", "r") as read_file:
            data = json.load(read_file)
            passenger_dict = data["passenger"]
            for passenger in passenger_dict:
                if passenger["passport"] == passport:
                    fname = passenger["first_name"]
                    lname = passenger["last_name"]
                    age = passenger["age"]
    except FileNotFoundError as err:
        return "File not found"

    # Add passenger to flights.json with the info gotten from passenger.json
    try:
        with open("flights.json", "r+") as read_file:
            data2 = json.load(read_file)
            for i in range(0, len(data2['flight_trip'])):
                if data2['flight_trip'][i]['id'] == flight_id:
                    info = {"passport": passport,
                            "first_name": fname,
                            "last_name": lname,
                            "age": age}
                    data2['flight_trip'][i]['passenger'].append(info)

                    read_file.seek(0)
                    json.dump(data2, read_file, indent=4)
    except FileNotFoundError as err:
        return "File not found"