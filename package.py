from enum import Enum
from datetime import datetime


class Priority(Enum):
    """An enumerator representing package priority"""

    HIGH = 3
    MEDIUM = 2
    LOW = 1


class Package():
    """A class representing a Package"""

    def __init__(self, id, location_id, deadline, mass, note=""):
        self.id = id
        self.location_id = location_id
        self.deadline = self._convert_deadline(deadline)
        self.mass = mass
        self.note = note
        self.priority = self._get_priority(self.deadline)

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
