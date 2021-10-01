from package import Package
from distance import Distance


class Graph:
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


p1 = Package(1, 2, "10:00 AM", 10.0)
p2 = Package(2, 3, "3:00 AM", 4.0)

d = Distance("distances.csv")

weight = d.all[p1.location_id][p2.location_id]

g = Graph()

g.add_package(p1)
g.add_package(p2)
g.add_edge(p1, p2, weight)
print(g.adjacency_list)
print(g.edge_weights)
