# Melanie Akau 000715019
from truck import Truck
import data
from decimal import Decimal

from datetime import time, date, datetime

total_distance = Decimal(0.0)
command = ""

truck1 = Truck(1, data.packages.get_truck(1), datetime.combine(
    date.today(), time(hour=8)), True)
truck2 = Truck(2, data.packages.get_truck(2), datetime.combine(
    date.today(), time(hour=9, minute=5)))
truck3 = Truck(3, data.packages.get_truck(3), datetime.combine(
    date.today(), time(hour=10, minute=20)))


truck1.start()
truck2.start()
print("Updating package 9 location address")
time_corrected = datetime.combine(date.today(), time(hour=10, minute=20))
data.packages.get_id(9).correct_location(20, time_corrected)
truck3.start()

total_distance += truck2.total_distance
total_distance += truck2.total_distance
total_distance += truck3.total_distance
print("Total distance travelled: " + str(total_distance))


def print_package_status_at(time):
    print("")
    print("PACKAGE STATUS AT: " + str(time))
    print("Truck  ID  Address                                 City        "
          + "      Zip    " "Mass  Deadline  Status     Delivery Time")
    print("-----  --  --------------------------------------  ------------"
          + "----  -----  ----  --------  ---------  -------------")
    truck1.print_packages(time)
    print("")
    truck2.print_packages(time)
    print("")
    truck3.print_packages(time)


def cmd_menu():
    print("Command Menu:")
    print("1) lookup")
    print("2) status")
    print("3) menu")
    print("4) exit")


def cmd_lookup():
    pkg_id = input("Input package id: ")


def cmd_status():
    try:
        timeformat = "%H:%M"
        my_time = input("Enter a time in military format (HH:MM): ")
        validtime = datetime.strptime(my_time, timeformat).time()
        time_to_check = datetime.combine(date.today(), validtime)
        print_package_status_at(time_to_check)
    except ValueError:
        print("Invalid time")


def process_command(command):
    if(command == "lookup" or command == "1"):
        cmd_lookup()
    elif(command == "status" or command == "2"):
        cmd_status()
    elif(command == "menu" or command == "3"):
        cmd_menu()
    elif(command == "exit" or command == "4"):
        print("Exiting program")
        quit()
    else:
        print("Invalid command")


cmd_menu()

while(True):
    command = input("Enter a command: ")
    process_command(command)
