from datetime import timedelta
import data
from decimal import Decimal
import nearestneighbor as nn
from package import Status
import copy


class Truck():
    """A class representing a truck"""

    # O(n^2)
    # Constructor
    def __init__(self, id, packages, start_time, is_returning=False):
        self.id = id
        self.speed = Decimal(18.0)
        self.total_distance = Decimal(0.0)
        self.start_time = start_time
        self.end_time = start_time
        self.current_loc = data.HUB_ID
        self.packages = packages
        self.path = self._calculate_path()
        self.is_returning = is_returning

    # O(n^2)
    # Calculate path using nearest neighbor algorithm
    def _calculate_path(self):
        return nn.calculate(self.packages)

    # O(1)
    # Add to total distance
    def add_distance(self, distance):
        self.total_distance += distance
    # O(1)
    # Add to total time

    def add_time(self, time_change):
        self.end_time += time_change

    # O(1)
    # Gets the time elapsed over a given distance
    # time elapsed = distance / speed
    def _calculate_time_change(self, distance):
        hours_elapsed = distance / self.speed
        change = timedelta(hours=float(hours_elapsed))
        return change

    # O(1)
    # Moves the truck and makes appropriate calculations to
    # total distance and time
    def go_to(self, location_id):
        distance = data.distances.get_distance(self.current_loc, location_id)
        self.add_distance(distance)
        time_change = self._calculate_time_change(distance)
        self.add_time(time_change)
        self.current_loc = location_id

    # O(n)
    def start(self):
        # O(n)
        # Set status of all packages to EN_ROUTE
        for k in self.packages.get_keys():
            package = self.packages.search(k).value
            package.status = Status.EN_ROUTE

        # O(n)
        # Deliver packages
        for next in self.path:
            package = self.packages.search(next).value
            self.go_to(package.location_id)
            package.set_delivered(self.end_time)
            package.check_on_time()

        # O(1)
        # Return the truck to hub if is_returning is set to True
        if self.is_returning:
            self.go_to(data.HUB_ID)
        # O(1)
        self.print_completion()

    # O(1)
    # Prints completion time and distance when the truck has completed its path
    def print_completion(self):
        print("Truck " + str(self.id) + " completed at: " + str(self.end_time))
        print("Distance travelled:  " + str(self.total_distance))

    # O(n^2)
    # print each package on the truck
    def print_packages(self, time):
        # O(n)
        for i in self.path:
            # O(n)
            pkg = self.packages.search(i).value

            # O(1)
            time_pkg = copy.copy(pkg)

            if self.start_time > time:
                time_pkg.status = Status.AT_THE_HUB
            else:
                time_pkg.status = Status.EN_ROUTE
            if pkg.delivery_time > time:
                time_pkg.delivery_time = None
            else:
                time_pkg.status = Status.DELIVERED

            # O(1)
            time_pkg.print_package(time)
