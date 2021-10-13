# Melanie Akau 000715019
from truck import Truck
import data
from decimal import Decimal

from datetime import time, date, datetime
total_distance = Decimal(0.0)

truck1 = Truck(1, data.packages.get(1), datetime.combine(
    date.today(), time(hour=8)), True)
truck1.start()
total_distance += truck1.total_distance
print("Truck 1 completed at " + str(truck1.end_time))
print("Distance travelled " + str(truck1.total_distance))

truck2 = Truck(2, data.packages.get(2), datetime.combine(
    date.today(), time(hour=9, minute=5)))
truck2.start()
total_distance += truck2.total_distance
print("Truck 2 completed at " + str(truck2.end_time))
print("Distance travelled " + str(truck2.total_distance))

print("Updating package 9 location address")
data.packages.get(3).search(9).value.location_id = 20
print(data.packages.get(3).search(9))
truck3 = Truck(3, data.packages.get(3), datetime.combine(
    date.today(), time(hour=10, minute=20)))
truck3.start()
total_distance += truck3.total_distance
print("Truck 3 completed at " + str(truck3.end_time))
print("Distance travelled " + str(truck3.total_distance))

print("Total distance travelled: " + str(total_distance))
