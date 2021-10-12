import data
from package import Priority


def calculate(packages):
    full_path = []
    queue = init_queue(packages)
    next_loc_id = data.HUB_ID
    high = get_priority_queue(Priority.HIGH, queue)
    med = get_priority_queue(Priority.MEDIUM, queue)
    low = get_priority_queue(Priority.LOW, queue)

    full_path.extend(nearest_neighbor(high, next_loc_id))
    print(full_path)
    if full_path != []:
        next_loc_id = packages.search(full_path[-1]).value.location_id
    full_path.extend(nearest_neighbor(med, next_loc_id))
    print(full_path)
    if full_path != []:
        next_loc_id = packages.search(full_path[-1]).value.location_id
    full_path.extend(nearest_neighbor(low, next_loc_id))
    print(full_path)
    return full_path


def nearest_neighbor(queue, start_id=data.HUB_ID):
    path = []
    current_loc_id = start_id

    while len(queue) > 0:
        nearest_distance = float('inf')
        nearest_package = None

        for pkg in queue:
            pkg_loc_id = pkg.location_id
            distance = data.distances.get_distance(pkg_loc_id, current_loc_id)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = pkg
        current_loc_id = nearest_package.location_id
        queue.remove(nearest_package)
        path.append(nearest_package.id)

    return path


def init_queue(packages):
    queue = []

    for i in packages.get_keys():
        package = packages.search(i).value
        queue.append(package)

    return queue


def get_priority_queue(priority, queue):
    new_queue = []
    for package in queue:
        if package.priority == priority:
            new_queue.append(package)
    return new_queue
