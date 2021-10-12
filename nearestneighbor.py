import data


def nearest_neighbor(packages, start_id=data.HUB_ID):
    path = []
    queue = init_queue(packages)
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
