# Melanie Akau 000715019
from truck import Truck
import data
from decimal import Decimal

from datetime import time, date, datetime

total_distance = Decimal(0.0)

truck1 = Truck(1, data.packages.get(1), datetime.combine(
    date.today(), time(hour=8)), True)
truck2 = Truck(2, data.packages.get(2), datetime.combine(
    date.today(), time(hour=9, minute=5)))
truck3 = Truck(3, data.packages.get(3), datetime.combine(
    date.today(), time(hour=10, minute=20)))


truck1.start()
truck2.start()
print("Updating package 9 location address")
data.packages.get(3).search(9).value.location_id = 20
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
    truck1.print_packages(time_to_check)
    print("")
    truck2.print_packages(time_to_check)
    print("")
    truck3.print_packages(time_to_check)


time_to_check = datetime.combine(date.today(), time(hour=10, minute=35))
print_package_status_at(time_to_check)
