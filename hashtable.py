import hashitemnode


class HashTable:
    """A class representing a hash table."""

    # O(1)
    def __init__(self, initial_size=10):
        self.initial_size = initial_size
        self.buckets = []
        self.keys = []
        self.is_empty = True
        for i in range(0, self.initial_size):
            new_bucket = []
            self.buckets.append(new_bucket)

    # O(1)
    def get_keys(self):
        return self.keys

    # O(1)
    def generate_hash_key(self, key):
        return hash(key) % len(self.buckets)

    # O(1)
    def get_bucket(self, key):
        hash_key = self.generate_hash_key(key)
        return self.buckets[hash_key]

    # O(n)
    def insert(self, key, value):
        self.is_empty = False
        bucket_list = self.get_bucket(key)
        for b in bucket_list:
            if b.key == key:
                b.value = value
                return True
        new_item = hashitemnode.HashItemNode(key, value)
        bucket_list.append(new_item)
        self.keys.append(key)
        return True

    # O(n) In the worst case scenario where each package is stored
    # in one bucket
    def search(self, key):
        bucket_list = self.get_bucket(key)
        for b in bucket_list:
            if b.key == key:
                return b
        return None

    # O(n)
    def remove(self, key):
        bucket_list = self.get_bucket(key)
        item_node = self.search(key)
        if item_node is not None:
            bucket_list.remove(item_node)
            return True
        else:
            return False

    # O(1)
    def __repr__(self):
        return str(self.buckets)
