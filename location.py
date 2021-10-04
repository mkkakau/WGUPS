import csv


class Location():
    """A class representing a location"""

    def __init__(self, id, address, city, state, zipcode, name):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.name = name

    def __repr__(self):
        text = ""
        text += "ID: " + self.id + ", "
        text += "Address: " + self.address + ", "
        text += "City: " + self.city + ", "
        text += "State: " + self.state + ", "
        text += "Zipcode: " + self.zipcode + ", "
        text += "Name: " + self.name
        return "[" + text + "]"


class LocationList():
    """A class holding a list of all locations"""

    def __init__(self, filename):
        self.filename = filename
        self.all = [None for x in range(28)]
        self._load_list(filename)

    def add_location(self, location):
        self.all[int(location.id)] = location

    def get(self, id):
        return self.all[id]

    def _load_list(self, filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                id = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zipcode = row[4]
                name = row[5]
                new_loc = Location(id, address, city, state, zipcode, name)
                self.add_location(new_loc)
