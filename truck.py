from datetime import timedelta
import data
from decimal import Decimal
import nearestneighbor as nn
from package import Status


class Truck():
    """A class representing a truck"""

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

    def _calculate_path(self):
        return nn.calculate(self.packages)

    def add_distance(self, distance):
        self.total_distance += distance

    def add_time(self, time_change):
        self.end_time += time_change

    def _calculate_time_change(self, distance):
        hours_elapsed = distance / self.speed
        change = timedelta(hours=float(hours_elapsed))
        return change

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

        # O(n)d
        # Deliver packages
        for next in self.path:
            package = self.packages.search(next).value
            self.go_to(package.location_id)
            package.set_delivered(self.end_time)
            package.check_on_time()

        if self.is_returning:
            self.go_to(data.HUB_ID)
