class HashItemNode:
    """A class representing a hash item node."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "[key: " + str(self.key) + ", value: " + str(self.value) + "]"
