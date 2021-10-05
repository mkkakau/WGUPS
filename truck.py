from datetime import timedelta, time, datetime, date
import data
from package import Status


class Truck():
    """A class representing a truck"""

    def __init__(self, id, packages, start_time):
        self.id = id
        self.speed = 18
        self.total_distance = 0
        self.start_time = start_time
        self.end_time = start_time
        self.current_loc = 1
        self.packages = packages
        self.path = self._calculate_path(packages)

    def _calculate_path(self, packages):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def add_distance(self, distance):
        self.total_distance += distance

    def add_time(self, time_change):
        self.end_time += time_change

    def _calculate_time_change(self, distance):
        hours_elapsed = distance / self.speed
        change = timedelta(hours=hours_elapsed)
        return change

    def go_to(self, location_id):
        distance = data.distances.get_distance(self.current_loc, location_id)
        self.add_distance(distance)
        time_change = self._calculate_time_change(distance)
        self.add_time(time_change)
        self.current_loc = location_id

    # O(2n)
    def start(self):
        # O(n) Set status of all packages to EN_ROUTE
        for k in self.packages.get_keys():
            package = self.packages.search(k).value
            package.status = Status.EN_ROUTE

        # O(n)
        for next in self.path:
            self.go_to(next)
            package = self.packages.search(next)
            package.status = Status.DELIVERED


t = Truck(1, data.packages.get(1), datetime.combine(
    date.today(), time(hour=8)))
print(t._calculate_time_change(0.6))
t.start()
