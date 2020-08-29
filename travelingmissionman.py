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


def check_constraints(systems, constraints):
    cur_prio = 0
    for item in systems:
        if cur_prio <= constraints[item]:
            cur_prio = constraints[item]
        else:
            return False
    return True


def check_name(name, system_ids, total_systems):
    try:
        system_id = system_ids[name]
    except KeyError:
        if name != "":
            print("Line", total_systems, ": Unable to find system {name}")
            return False
    return True


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
    total_lines = 0
    using_constraints = False
    constraints = {}
    with open('missions.txt') as input_file:
        for line in input_file:
            total_lines += 1
            array = line.strip().split(',')
            system_one_name = array[0]
            found_system_one = check_name(system_one_name, system_ids, total_lines)
            if found_system_one and system_one_name != "":
                system_one_id = system_ids[system_one_name]
                system_ids.append(system_one_id)
            if len(array) > 2:
                print("Line", total_lines, ": Only 2 systems per line in constraints system.")
            elif len(array) == 2:
                system_two_name = array[2]
                found_system_two = check_name(system_two_name, system_ids, total_lines)
                if found_system_two and system_two_name != "":
                    constraints[system_one_id]
            try:
                found_systems = check_name(system_name, system_ids, total_lines) and found_systems
                try:
                    system_id = system_ids[system_name]
                except KeyError:
                    found_systems = False
                    print("Unable to find system", system_name)
                mission_systems.append(array[1])
                using_constraints = True
            except IndexError:
                constraints[system_id] = None
            mission_systems.append(system_id)
    start_system = [mission_systems.pop(0)]
    if found_systems is False:
        print("Could not find all the systems in missions.txt, please check and retry.")
        exit()
    if total_lines < 2:
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
        if using_constraints:
            valid_priority = check_constraints(permutation, constraints)
            if not valid_priority:
                continue
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
    print("Total distance", min_path_distance, "jumps.")
    # print(short_systems, min_path_distance)


if __name__ == "__main__":
    main()
