from enum import Enum
from datetime import datetime, date, time
from hashtable import HashTable
import data
import csv


# O(1)
class Priority(Enum):
    """An enumerator representing package priority"""

    HIGH = 3
    MEDIUM = 2
    LOW = 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


# O(1)
class Status(Enum):
    """An enumerator representing package delivery status."""

    AT_THE_HUB = 0
    EN_ROUTE = 1
    DELIVERED = 2

    def __repr__(self):
        return self.name.replace("_", " ")

    def __str__(self):
        return self.__repr__()


class Package():
    """A class representing a Package"""

    # O(1)
    # Constructor
    def __init__(self, id, truck_id, location_id, deadline, mass, note=""):
        self.id = int(id)
        self.truck_id = int(truck_id)
        self.location_id = int(location_id)
        self.location = data.locations.get(location_id)
        self.deadline = self._convert_deadline(deadline)
        self.mass = mass
        self.note = note
        self.priority = self._get_priority(self.deadline)
        self.status = Status.AT_THE_HUB
        self.delivery_time = None
        self.is_corrected = False
        self.corrected_location_id = None
        self.correction_time = None

    # O(1)
    # Takes the time string from file and converts to datetime object
    def _convert_deadline(self, deadline):
        today = date.today()
        if deadline == "EOD":
            dl = time(hour=23, minute=59, second=59)
        else:
            format = "%H:%M %p"
            dl = datetime.strptime(deadline, format).time()
        formatted = datetime.combine(today, dl)
        return formatted

    # O(1)
    def _get_priority(self, deadline):
        priority = Priority.LOW
        today = date.today()
        if deadline == datetime.combine(today, time(hour=9)):
            priority = Priority.HIGH
        if deadline == datetime.combine(today, time(hour=10, minute=30)):
            priority = Priority.MEDIUM
        return priority

    # O(1)
    def set_delivered(self, time):
        self.delivery_time = time
        self.status = Status.DELIVERED

    # O(1)
    def correct_location(self, corrected_location_id, correction_time):
        self.is_corrected = True
        self.corrected_location_id = corrected_location_id
        self.correction_time = correction_time

    # O(1)
    def check_on_time(self):
        if self.delivery_time is None:
            print("Package has not been delivered. Cannot calculate on_time()")
        if self.delivery_time > self.deadline:
            print("Package " + str(self.id) + " did not meet deadline.")

    # O(1)
    # Format and print the package given a time that defaults to EOD
    def print_package(self, time=datetime.combine(date.today(),
                                                  time(hour=23,
                                                       minute=59,
                                                       second=59))):
        if(self.is_corrected and time >= self.correction_time):
            location = data.locations.get(self.corrected_location_id)
        else:
            location = data.locations.get(self.location_id)

        dt_format = "%H:%M:%S"
        formatted = ""
        formatted += f"{self.truck_id:>5}" + "  "
        formatted += f"{self.id:0>2}" + "  "
        formatted += f"{location.address:<38}" + "  "
        formatted += f"{location.city:<16}" + "  "
        formatted += f"{location.zipcode:<5}" + "  "
        formatted += f"{self.mass:>4}" + "  "
        formatted += self.deadline.strftime(dt_format) + "  "
        formatted += f"{self.status:<9}" + "  "
        if self.delivery_time is not None:
            formatted += f"{self.delivery_time.strftime(dt_format)}"
        print(formatted)


class PackageList():
    """A class representing a list of packages."""

    # O(n)
    # Constructor
    def __init__(self, filename):
        self.filename = filename
        self.all = self._load_list(filename)

    # O(n)
    # Load the packages from the csv file
    def _load_list(self, filename):

        table = HashTable()

        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                id = int(row[0])
                location_id = int(row[1])
                deadline = row[2]
                mass = row[3]
                note = row[4]
                truck = int(row[5])
                package = Package(id, truck, location_id, deadline, mass, note)
                table.insert(id, package)
        return table

    # O(n)
    # Find packages with the given truck id
    def get_truck(self, truck_id):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.truck_id == truck_id:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find the package with the given id
    def get_id(self, id):
        # O(n)
        package = self.all.search(id)
        if package is None:
            raise ValueError
        return package.value

    # O(n)
    # Find packages with the given address
    def get_address(self, address):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.location.address == address:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find packages with the given deadline
    def get_deadline(self, deadline):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.deadline == deadline:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find packages with the given city
    def get_city(self, city):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.location.city == city:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find packages with the given zipcode
    def get_zipcode(self, zipcode):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.location.zipcode == zipcode:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find packages with the given mass
    def get_mass(self, mass):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.mass == mass:
                packages.insert(p, package)
        return packages

    # O(n)
    # Find packages with the given status
    def get_status(self, status):
        packages = HashTable()
        for p in self.all.get_keys():
            package = self.all.search(p).value
            if package.status == status:
                packages.insert(p, package)
        return packages
