class Distance():
    """A class """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.list = []

    def add_distance(self, loc_id1, loc_id2, distance):
        self.list[loc_id1][loc_id2] = distance
        self.list[loc_id2][loc_id1] = distance

    def get_distance(self, location1, location2):
        return self.list[location1.id][location2.id]
