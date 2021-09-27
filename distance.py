import csv


class Distance():
    """A class """

    def __init__(self, filename):
        self.filename = filename
        self.list = [[None for x in range(28)] for i in range(28)]
        self._load_list(filename)

    def add_distance(self, loc_id1, loc_id2, distance):
        self.list[loc_id1][loc_id2] = distance
        self.list[loc_id2][loc_id1] = distance

    def get_distance(self, location1, location2):
        return self.list[location1.id][location2.id]

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


d = Distance("distances.csv")
print(d.list[6][27])
