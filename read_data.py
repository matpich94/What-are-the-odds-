# This function takes the path of the universe.db file
# and transforms it into a list which can be easily processed
def read_routes(path):
    import sqlite3
    
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute("SELECT ORIGIN, DESTINATION, TRAVEL_TIME FROM ROUTES;")
    results = cursor.fetchall()
    routes = []
    
    for r in results:
        routes.append(r)
    cursor.close()
    
    connection.close()    
    return (routes)

# This function reads the millenium-falcon.json file
# and returns the autonomy and the routes file as a list
def read_millenium_falcon(path):
    import json
    millenium_falcon = json.load(open(path))  
    if ('autonomy' not in millenium_falcon.keys()) or ('routes_db' not in millenium_falcon.keys()):
        return (0, [])
    else:
        autonomy = millenium_falcon['autonomy']
        routes = read_routes(millenium_falcon['routes_db'])    
        return (autonomy, routes)
    
# The 3 following functions are used to compute all of the possible
# paths between Tatooine and Endore according to the universe.db file

# This first function creates an initial list of 
# path between Tatooine and the reachable planet from Tatooine
# according to the routes list
def initialisation (routes):
    paths = []
    for el in routes:
        if el[0] == 'Tatooine':
            paths.append([(el[0], 0), (el[1], el[2])])
            
    return paths

# This function returns True once all of the paths 
# have been computed
def all_paths_bool (paths):
    counter = 0
    for el in paths:
        if el[-1][0] != 'Endor':
            return False
        
    return True
    
# This function takes the list of route previously
# processed (from the universe.db file) and retourn 
# all of the different paths as a list of list.
# Each list of the list is a path composed of tuples (str(Planet Name), int(day to reach it))
def create_all_paths (routes):
    final_paths = []
    previous_paths = initialisation(routes)
    while not(all_paths_bool(previous_paths)):
        new_multiple_paths = []
        for path in previous_paths:
            for option in routes:
                if path[-1][0] == option[0]:
                    virgin_path = list(path)
                    virgin_path.append((option[1], path[-1][1] + option[2]))   
                    if virgin_path[-1][0] == 'Endor':
                        final_paths.append(virgin_path)
                    new_multiple_paths.append(virgin_path)
        previous_paths = list(new_multiple_paths)
    return final_paths

    
# This function reads the empire-json.file
# and returns the countdown and the map of the hunters
def read_empire(path):
    import json

    empire = json.loads(open(path).read())
    
    if ('countdown' not in empire.keys()) or ('bounty_hunters' not in empire.keys()):
        return (0, [])
    else:
        countdown = empire['countdown']    
        hunters = []    
        for el in empire['bounty_hunters']:
            hunters.append((el['planet'], el['day']))
            
    return (countdown, hunters)