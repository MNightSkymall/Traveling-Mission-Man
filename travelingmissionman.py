import json, itertools
from datetime import datetime

def calculate_distance(systems, distances):
    dist = 0
    for i in range(len(systems)-1):
        first_system = systems[i]
        second_system = systems[i+1]
        distances[first_system][second_system]
        dist += distances[systems[i]][systems[i+1]]
    return dist

def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Begin at", current_time)
    with open("output.json") as input:
        distances = json.load(input)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Finished loading json at", current_time)
    print(distances['30000142'])
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
    with open('missions.txt') as input_file:
        for line in input_file:
            system_name = line.strip()
            system_id = system_ids[system_name]
            mission_systems.append(system_id)

    min_path_distance = 1000000000

    for permutation in itertools.permutations(mission_systems):
        distance = calculate_distance(permutation, distances)
        if distance < min_path_distance:
            shortest_path = permutation
            min_path_distance = distance
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Found shortest_path at",current_time)
    short_systems = []
    for item in shortest_path:
        short_systems.append(names[item])
    print(short_systems, min_path_distance)



if __name__ == "__main__":
    main()
