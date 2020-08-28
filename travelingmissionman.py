import json, itertools
from datetime import datetime


def calculate_distance(systems, distances):
    dist = 0
    for i in range(len(systems) - 1):
        first_system = systems[i]
        second_system = systems[i + 1]
        distances[first_system][second_system]
        dist += distances[systems[i]][systems[i + 1]]
    return dist


def main():
    names = {}
    system_ids = {}
    with open("systems.csv") as system_names:
        header = system_names.readline()
        for line in system_names:
            array = line.strip().split(",")
            system_id = array[0].strip()
            system_name = array[4].strip()
            names[system_id] = system_name
            system_ids[system_name] = system_id

    mission_systems = []
    found_systems = True
    total_systems = 0
    with open('missions.txt') as input_file:
        for line in input_file:
            total_systems += 1
            system_name = line.strip()
            try:
                system_id = system_ids[system_name]
            except KeyError:
                found_systems = False
                print("Unable to find system", system_name)
            mission_systems.append(system_id)
    start_system = [mission_systems.pop(0)]
    if found_systems is False:
        print("Could not find all the systems in missions.txt, please check and retry.")
        exit()
    if total_systems < 2:
        print("Requires at least 2 systems.")
        exit()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Begin at", current_time)
    with open("output.json") as input:
        distances = json.load(input)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Finished loading json at", current_time)

    min_path_distance = 1000000000

    for permutation in itertools.permutations(mission_systems):
        total_path = tuple(start_system) + permutation
        distance = calculate_distance(total_path, distances)
        if distance < min_path_distance:
            shortest_path = total_path
            min_path_distance = distance
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Found shortest_path at", current_time)
    short_systems = []
    for i in range(len(shortest_path) - 1):
        first_system_id = shortest_path[i]
        second_system_id = shortest_path[i + 1]
        first_system_name = names[first_system_id]
        second_system_name = names[second_system_id]
        jump_distance = distances[first_system_id][second_system_id]
        print(first_system_name, "->", jump_distance, "jumps ->", second_system_name)
        # print(names)
        # short_systems.append(names[item])
    print("Total distance",min_path_distance,"jumps.")
    # print(short_systems, min_path_distance)


if __name__ == "__main__":
    main()
