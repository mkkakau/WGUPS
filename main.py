# Melanie Akau 000715019
import data
from decimal import Decimal
from truck import Truck
from datetime import time, date, datetime
from hashtable import HashTable
from package import Status


def main():

    # O(n^2)
    # Initialize trucks
    truck1 = Truck(1, data.packages.get_truck(1), datetime.combine(
        date.today(), time(hour=8)), True)
    truck2 = Truck(2, data.packages.get_truck(2), datetime.combine(
        date.today(), time(hour=9, minute=5)))
    truck3 = Truck(3, data.packages.get_truck(3), datetime.combine(
        date.today(), time(hour=10, minute=20)))
    trucks = [truck1, truck2, truck3]

    # O(1)
    # Update package 9 location to correct address
    print("Updating package 9 location address")
    time_corrected = datetime.combine(date.today(), time(hour=10, minute=20))
    data.packages.get_id(9).correct_location(20, time_corrected)

    # O(1)
    # Start the trucks
    start_trucks(trucks)

    # O(1)
    # Print total distance travelled
    print_total_distance(trucks)

    # Wait for input and process command
    while(True):
        process_command(trucks)


# O(1)
def start_trucks(trucks):
    for truck in trucks:
        truck.start()


def process_command(trucks):
    cmd_menu()
    command = input("Enter a command: ").lower()
    if(command == "lookup" or command == "1"):
        process_lookup_command()
    elif(command == "status" or command == "2"):
        cmd_status(trucks)
    elif(command == "exit" or command == "3"):
        print("Exiting program")
        quit()
    else:
        print("Invalid command")


# O(n)
def process_lookup_command():
    cmd_lookup_menu()
    command = input("Enter a field to lookup: ").lower()
    packages = HashTable()
    if(command == "1" or command == "id"):
        packages = lookup_pkgs_id()
    elif(command == "2" or command == "address"):
        packages = lookup_pkgs_address()
    elif(command == "3" or command == "deadline"):
        packages = lookup_pkgs_deadline()
    elif(command == "4" or command == "city"):
        packages = lookup_pkgs_city()
    elif(command == "5" or command == "zipcode"):
        packages = lookup_pkgs_zipcode()
    elif(command == "6" or command == "mass"):
        packages = lookup_pkgs_mass()
    elif(command == "7" or command == "status"):
        packages = lookup_pkgs_status()
    else:
        print("Invalid command")

    print_header()
    if packages.is_empty:
        print("No packages found.")
    else:
        print_lookup(packages)


def lookup_pkgs_id():
    packages = HashTable()
    try:
        id = int(input("Enter id: "))
        packages.insert(id, data.packages.get_id(id))
    except ValueError:
        print("Invalid id")
    return packages


def lookup_pkgs_address():
    address = input("Enter address: ")
    return data.packages.get_address(address)


def lookup_pkgs_deadline():
    time_to_check = get_time()
    return data.packages.get_deadline(time_to_check)


def get_time():
    try:
        my_time = input("Enter a time in military format (HH:MM): ")
        timeformat = "%H:%M"
        validtime = datetime.strptime(my_time, timeformat).time()
        time_to_check = datetime.combine(date.today(), validtime)
        return time_to_check
    except ValueError:
        print("Invalid time")


def lookup_pkgs_city():
    city = input("Enter city: ")
    return data.packages.get_city(city)


def lookup_pkgs_zipcode():
    zipcode = input("Enter zipcode: ")
    return data.packages.get_zipcode(zipcode)


def lookup_pkgs_mass():
    mass = input("Input mass: ")
    return data.packages.get_mass(mass)


def lookup_pkgs_status():
    return data.packages.get_status(Status.DELIVERED)


def cmd_status(trucks):

    time_to_check = get_time()
    print_header(time_to_check)
    print_package_status_at(time_to_check, trucks)

# O(1)
# Prints the main command menu


def cmd_menu():
    print("")
    print("Command Menu:")
    print("1) lookup")
    print("2) status")
    print("3) exit")
    print("")

# O(1)
# Prints the menu of commands avaiable from the lookup function


def cmd_lookup_menu():
    print("")
    print("Lookup packages by:")
    print("1) ID")
    print("2) Address")
    print("3) Deadline")
    print("4) City")
    print("5) Zipcode")
    print("6) Mass")
    print("7) Status")
    print("")


# O(1)
# The header for the package table
def print_header(my_time=datetime.combine(date.today(), time(hour=23,
                                                             minute=59,
                                                             second=59))):
    print("")
    print("PACKAGE STATUS AT: " + str(my_time))
    print("Truck  ID  Address                                 City        "
          + "      Zip    " "Mass  Deadline  Status     Delivery Time")
    print("-----  --  --------------------------------------  ------------"
          + "----  -----  ----  --------  ---------  -------------")


# O(n^2)
# Print the package status at a given time from all trucks
def print_package_status_at(my_time, trucks):
    for truck in trucks:
        truck.print_packages(my_time)
        print("")


# O(t)
# Prints the total distance travelled from all trucks
def print_total_distance(trucks):
    total_distance = Decimal(0.0)
    for truck in trucks:
        total_distance += truck.total_distance
    print("Total distance travelled: " + str(total_distance))


# O(n^2)
# Prints a hashtable of packages
def print_lookup(packages):
    for key in packages.get_keys():
        package = packages.search(key).value
        package.print_package()


if __name__ == "__main__":
    main()
