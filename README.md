# Traveling-Mission-Man
Start by running precompute.py to generate the json file for travelingmissionman.py

Input system names, cap sensitive, into missions.txt and then run travelingmissionman.py
It outputs an optimal list of jumps from system to system. It assumes that the first system in the list is the desired start system.

systems.csv includes a list of all systems in Eve Echoes by name and system id and their neighbors.
output.json is a hash of hashes storing the number of jumps between systems by systemid.

Example output:   
Bridi -> 3 jumps -> Noranim   
Noranim -> 2 jumps -> Gayar   
Gayar -> 2 jumps -> Petidu   
Petidu -> 8 jumps -> Jedandan   
Jedandan -> 7 jumps -> Daran   
Daran -> 10 jumps -> Keshirou   
Keshirou -> 8 jumps -> Sibot   
Sibot -> 7 jumps -> Porsharrah   
Total distance 47 jumps.   
