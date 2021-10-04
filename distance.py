import csv


class DistanceList():
    """A class holding all distance data betweeen all locations"""

    def __init__(self, filename):
        self.filename = filename
        self.all = [[None for x in range(28)] for i in range(28)]
        self._load_list(filename)

    def add_distance(self, loc_id1, loc_id2, distance):
        self.all[loc_id1][loc_id2] = distance
        self.all[loc_id2][loc_id1] = distance

    def get_distance(self, loc_id1, loc_id2):
        return self.all[loc_id1][loc_id2]

    def _load_list(self, filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                id1 = int(row[0])
                for i, distance in enumerate(row):
                    if i == 0:
                        continue
                    else:
                        self.add_distance(id1, i, distance)
