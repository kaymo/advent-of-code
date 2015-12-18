import itertools

# Comparative constants
MAX_ROUTE_LENGTH = 10000000000
MIN_ROUTE_LENGTH = 0
INVALID_LENGTH   = -1 

# Legs
input = ["Faerun to Tristram = 65", "Faerun to Tambi = 129", "Faerun to Norrath = 144", "Faerun to Snowdin = 71", "Faerun to Straylight = 137", "Faerun to AlphaCentauri = 3", "Faerun to Arbre = 149", "Tristram to Tambi = 63", "Tristram to Norrath = 4", "Tristram to Snowdin = 105", "Tristram to Straylight = 125", "Tristram to AlphaCentauri = 55", "Tristram to Arbre = 14", "Tambi to Norrath = 68", "Tambi to Snowdin = 52", "Tambi to Straylight = 65", "Tambi to AlphaCentauri = 22", "Tambi to Arbre = 143", "Norrath to Snowdin = 8", "Norrath to Straylight = 23", "Norrath to AlphaCentauri = 136", "Norrath to Arbre = 115", "Snowdin to Straylight = 101", "Snowdin to AlphaCentauri = 84", "Snowdin to Arbre = 96", "Straylight to AlphaCentauri = 107", "Straylight to Arbre = 14", "AlphaCentauri to Arbre = 46"]

# Get a list of unique locations and the distances between each pair
locations = []
distances = {}

for travel in input:
    locations.append(travel.split()[0])
    locations.append(travel.split()[2])
    
    distances[travel.split(" = ")[0]] = int(travel.split(" = ")[1])
    
locations = list(set(locations))

# Test each permutation of route legs to find the shortest and longest routes
min_route_length = MAX_ROUTE_LENGTH
max_route_length = MIN_ROUTE_LENGTH

min_route = 0
max_route = 0

for route in itertools.permutations(locations):

    route_distance = 0
    
    for i in xrange(0, len(route)-1):
    
        leg_1 = route[i]   + " to " + route[i+1]
        leg_2 = route[i+1] + " to " + route[i]
        
        if leg_1 in distances:
            route_distance += distances[ leg_1 ]
        elif leg_2 in distances:
            route_distance += distances[ leg_2 ]
        else:
            print "Error: unexpected route: {}".format(leg)
            route_distance = INVALID_LENGTH
            break;
        
    # Compare to minimum and maximum route lengths seen so far
    if not route_distance == INVALID_LENGTH:
        if route_distance < min_route_length:
            min_route_length = route_distance
            min_route = route
        
        elif route_distance > max_route_length:
            max_route_length = route_distance
            max_route = route
  
# Part One  
print "Part One: Shortest route distance: {}".format(min_route)
print min_route_length

# Part Two
print "Part One: Longest route distance: {}".format(max_route)
print max_route_length
        

