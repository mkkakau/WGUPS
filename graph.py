class Graph:
    """A class representing a graph."""

    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_package(self, package):
        self.adjacency_list[package.id] = []

    def add_edge(self, package1, package2, weight):
        self.edge_weights[package1.id, package2.id] = weight
        self.edge_weights[package1.id, package2.id] = weight
        self.adjacency_list[package1.id].append(package2)
        self.adjacency_list[package2.id].append(package1)
