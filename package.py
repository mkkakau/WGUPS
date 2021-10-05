from enum import Enum
from datetime import datetime
from hashtable import HashTable
import csv


class Priority(Enum):
    """An enumerator representing package priority"""

    HIGH = 3
    MEDIUM = 2
    LOW = 1


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

    def __init__(self, id, location_id, deadline, mass, note=""):
        self.id = int(id)
        self.location_id = int(location_id)
        self.deadline = self._convert_deadline(deadline)
        self.mass = mass
        self.note = note
        self.priority = self._get_priority(self.deadline)
        self.status = Status.AT_THE_HUB

    def _convert_deadline(self, deadline):
        format_data = "%H:%M %p"
        formatted_deadline = datetime.strptime(deadline, format_data).time()
        return formatted_deadline

    def _get_priority(self, deadline):
        priority = Priority.LOW
        if deadline == "9:00 AM":
            priority = Priority.HIGH
        if deadline == "10:30 AM":
            priority = Priority.MEDIUM
        return priority

    def __repr__(self):
        text = ""
        text += "ID: " + str(self.id) + ", "
        text += "Location ID: " + str(self.location_id) + ", "
        text += "Deadline: " + str(self.deadline) + ", "
        text += "Mass: " + self.mass + ", "
        text += "Note: " + self.note + ", "
        text += "Status: " + str(self.status) + ", "
        text += "Priority: " + str(self.priority)
        return "{" + text + "}"

    def __str__(self):
        return self.__repr__()


class PackageList():
    """A class representing a list of packages."""

    def __init__(self, filename):
        self.filename = filename
        self.all = self._load_list(filename)

    def _load_list(self, filename):

        truck1 = HashTable()
        truck2 = HashTable()
        truck3 = HashTable()

        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                id = int(row[0])
                location_id = int(row[1])
                deadline = row[2]
                mass = row[3]
                note = row[4]
                package = Package(id, location_id, deadline, mass, note)
                truck1.insert(id, package)
        list = [None, truck1, truck2, truck3]
        return list

    # O(1)
    def get(self, truck_id):
        return self.all[truck_id]
