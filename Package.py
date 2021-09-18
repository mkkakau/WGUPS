class Package():
    """A class representing a Package"""

    def __init__(self, id, location_id, deadline, mass, note):
        self.id = id
        self.location_id = location_id
        self.deadline = deadline
        self.mass = mass
        self.note = note
