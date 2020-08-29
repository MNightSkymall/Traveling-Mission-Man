# Traveling-Mission-Man
precompute.py generates the json file for travelingmissionman.py, but the included json in the repo has all systems outside of nullsec and should be fine.


Input system names, cap sensitive, into missions.txt and then run travelingmissionman.py   
It outputs an optimal list of jumps from system to system. It assumes that the first system in the list is the desired start system.

### New constraint system
Input up to 2 systems into missions.txt separated by a comma, and it will constrain the search so that those two systems
are done in order. The missions.txt example in this version has example syntax.

systems.csv includes a list of all systems in Eve Echoes by name and system id and their neighbors.
output.json is a hash of hashes storing the number of jumps between systems by systemid.

Example output:   
Bridi -> 3 jumps -> Noranim   
Noranim -> 3 jumps -> Petidu   
Petidu -> 2 jumps -> Gayar   
Gayar -> 7 jumps -> Jedandan   
Jedandan -> 7 jumps -> Daran   
Daran -> 10 jumps -> Keshirou   
Keshirou -> 8 jumps -> Sibot    
Sibot -> 7 jumps -> Porsharrah   
Porsharrah -> 14 jumps -> Sifilar   
Sifilar -> 6 jumps -> Haras   
Haras -> 2 jumps -> Saikamon   
Total distance 69 jumps.   
Nice.   

Process finished with exit code 0

