# Traveling-Mission-Man
Start by running precompute.py to generate the json file for travelingmissionman.py

Input system names, cap sensitive, into missions.txt and then run travelingmissionman.py
It outputs an unformatted list in optimal order and the total number of jumps.

systems.csv includes a list of all systems in Eve Echoes by name and system id and their neighbors.
output.json is a hash of hashes storing the number of jumps between systems by systemid.