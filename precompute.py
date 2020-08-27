import queue
import json


def get_distances(nodes, start_node):
    visited = {}
    distances = {}
    for node in nodes.keys():
        visited[node] = False
        distances[node] = 100000000
    to_visit = queue.Queue()
    to_visit.put(start_node)
    visited[start_node] = True
    distances[start_node] = 0
    while not to_visit.empty():
        node = to_visit.get()
        for neighbor in nodes[node]:
            try:
                distances[neighbor] = min(distances[neighbor], distances[node] + 1)
                if visited[neighbor] is not True:
                    to_visit.put(neighbor)
                    visited[neighbor] = True
            except KeyError:
                pass
    return distances


def compute():
    nodes = {}
    with open('systems.csv') as systems:
        header = systems.readline()
        for line in systems:
            array = line.strip().split(',')
            system_id = int(array[0])
            security = float(array[5])
            if security > -5:
                neighbors = []
                for x in array[6].strip().split(':'):
                    try:
                        neighbors.append(int(x))
                    except ValueError:
                        pass
                nodes[system_id] = neighbors

    distances = {}
    total_systems = 0
    for start_node in nodes.keys():
        distances[start_node] = get_distances(nodes, start_node)
        total_systems += 1
        if total_systems % 10 == 0:
            print(total_systems)
    output_systems = {}
    with open("systems.csv") as highsec:
        header = highsec.readline()
        for line in highsec:
            array = line.strip().split(',')
            system_id = int(array[0])
            security = float(array[5])
            output_systems[system_id] = distances[system_id]
    with open("output.json",'w') as output:
        json.dump(output_systems,output)

if __name__ == "__main__":
    compute()
