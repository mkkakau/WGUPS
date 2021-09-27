class HashItemNode:
    """A class representing a hash item node."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "[key: " + str(self.key) + ", value: " + str(self.value) + "]"


class HashTable:
    """A class representing a hash table."""

    def __init__(self, initial_size=10):
        self.initial_size = initial_size
        self.buckets = []
        for i in range(0, self.initial_size):
            new_bucket = []
            self.buckets.append(new_bucket)

    def generate_hash_key(self, key):
        return hash(key) % len(self.buckets)

    def get_bucket(self, key):
        hash_key = self.generate_hash_key(key)
        return self.buckets[hash_key]

    def insert(self, key, value):
        bucket_list = self.get_bucket(key)
        for b in bucket_list:
            if b.key == key:
                b.value = value
                return True
        new_item = HashItemNode(key, value)
        bucket_list.append(new_item)
        return True

    def search(self, key):
        bucket_list = self.get_bucket(key)
        for b in bucket_list:
            if b.key == key:
                return b
        return None

    def remove(self, key):
        bucket_list = self.get_bucket(key)
        item_node = self.search(key)
        if item_node is not None:
            bucket_list.remove(item_node)
            return True
        else:
            return False

    def __repr__(self):
        return str(self.buckets)


test_hash = HashTable()
test_hash.insert(32, "hi")
test_hash.insert(32, "hi2")
test_hash.insert(42, "hi3")
test_hash.insert(33, "boop")
searched = test_hash.search(32)
print(test_hash)
print(searched)
print("Removed = " + str(test_hash.remove(42)))
print(test_hash)
