# Melanie Akau 000715019
import data
from decimal import Decimal
from truck import Truck
from datetime import time, date, datetime


def main():

    # Initialize trucks
    truck1 = Truck(1, data.packages.get_truck(1), datetime.combine(
        date.today(), time(hour=8)), True)
    truck2 = Truck(2, data.packages.get_truck(2), datetime.combine(
        date.today(), time(hour=9, minute=5)))
    truck3 = Truck(3, data.packages.get_truck(3), datetime.combine(
        date.today(), time(hour=10, minute=20)))
    trucks = [truck1, truck2, truck3]

    # Update package 9 location to correct address
    print("Updating package 9 location address")
    time_corrected = datetime.combine(date.today(), time(hour=10, minute=20))
    data.packages.get_id(9).correct_location(20, time_corrected)

    # Start the trucks
    start_trucks(trucks)

    # Print total distance travelled
    print_total_distance(trucks)

    # Display command menu
    cmd_menu()

    # Wait for input and process command
    command = ""
    while(True):
        command = input("Enter a command: ")
        process_command(command, trucks)


def start_trucks(trucks):
    for truck in trucks:
        truck.start()


def process_command(command, trucks):
    if(command == "lookup" or command == "1"):
        cmd_lookup()
    elif(command == "status" or command == "2"):
        cmd_status(trucks)
    elif(command == "menu" or command == "3"):
        cmd_menu()
    elif(command == "exit" or command == "4"):
        print("Exiting program")
        quit()
    else:
        print("Invalid command")


def cmd_lookup():
    pkg_id = input("Input package id: ")
    print("TODO: " + str(pkg_id))


def cmd_status(trucks):
    try:
        timeformat = "%H:%M"
        my_time = input("Enter a time in military format (HH:MM): ")
        validtime = datetime.strptime(my_time, timeformat).time()
        time_to_check = datetime.combine(date.today(), validtime)
        print_header(time_to_check)
        print_package_status_at(time_to_check, trucks)
    except ValueError:
        print("Invalid time")


def cmd_menu():
    print("Command Menu:")
    print("1) lookup")
    print("2) status")
    print("3) menu")
    print("4) exit")


def print_header(my_time):
    print("")
    print("PACKAGE STATUS AT: " + str(my_time))
    print("Truck  ID  Address                                 City        "
          + "      Zip    " "Mass  Deadline  Status     Delivery Time")
    print("-----  --  --------------------------------------  ------------"
          + "----  -----  ----  --------  ---------  -------------")


def print_package_status_at(my_time, trucks):
    for truck in trucks:
        truck.print_packages(my_time)
        print("")


def print_total_distance(trucks):
    total_distance = Decimal(0.0)
    for truck in trucks:
        total_distance += truck.total_distance
    print("Total distance travelled: " + str(total_distance))


if __name__ == "__main__":
    main()
