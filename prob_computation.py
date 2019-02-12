"""
This script is used to compute the probability
of being captured according to the following parameters:
autonomy, countdown, routes, bounty_hunters.
"""

import math

# This function computes the minimal time needed by the falcon to reach Endor
# by refueling the minimal number of times
def time_needed (path, autonomy):
    number_refuels = math.floor(path[-1][1] / autonomy )
    return (path[-1][1] + number_refuels)

# This function computes the number of times the bounty hunters will hunt 
# the falcon millenium if the time needed by the falcon millenium to reach Endor
# corresponds exactly to the countdown
def number_hunt_exact_day (path, hunters, autonomy):
    hunts_counter = 0
    refuel_counter = 0    
    for i in range(len(path) - 1):
        if (path[i][0], path[i][1] + refuel_counter) in hunters:
            hunts_counter += 1
            
        if path[i + 1][1] > (refuel_counter + 1) * autonomy: #Needs to refuel
            refuel_counter += 1
            if (path[i][0], path[i][1] + refuel_counter) in hunters:
                hunts_counter += 1 
        
    return (hunts_counter)
    

# This function computes the number of times the bounty hunters will hunt 
# the falcon millenium if the time needed by the falcon millenium to reach Endor 
# is greater than the countdown
def number_hunt_extra_days (path, hunters, autonomy, time_needed):
    extra_days = time_needed - path[-1][1]
    hunts_counter = 0
    refuel_counter = 0
    days_to_wait = 0
    
    for i in range(len(path) - 1):
        # You can leave or have to leave
        if (path[i][0], path[i][1] + refuel_counter + days_to_wait) in hunters:
            hunts_counter += 1
        
        if path[i + 1][1] > (refuel_counter + 1) * autonomy:
            refuel_counter += 1
            if (path[i][0], path[i][1] + refuel_counter + days_to_wait) in hunters:
                hunts_counter += 1
                
            
            
        if (path[i + 1][0], path[i + 1][1]  + refuel_counter + days_to_wait) in hunters:
            stay = True
            while extra_days > 0 and stay:
                days_to_wait += 1
                if (path[i + 1][0], path[i + 1][1]  + refuel_counter + days_to_wait) in hunters:
                    stay = True
                    extra_days -= 1
                else:
                    stay = False
        
    return hunts_counter
                
                

# This function computes the probabily of being captured by the bounty hunters
# according to the number of hunts they will carry out
def compute_prob(hunts_counter):
    prob = 0
    for i in range(hunts_counter):
        prob += (9 ** i) / (10 ** (i + 1))
    return (100*(1 - prob))
    
# This function computes the best probability of the millenium falcon
# to reach Endor according to the different possible paths
def compute_final_prob (paths, autonomy, countdown, hunters):
    prob = []
    for el in paths:
        time = time_needed(el, autonomy)
        if time > countdown:
            prob.append(0)

        if time == countdown:
            hunts_counter = number_hunt_exact_day (el, hunters, autonomy)
            prob.append(compute_prob(hunts_counter))

        if time < countdown:
            hunts_counter = number_hunt_extra_days (el, hunters, autonomy, time)
            prob.append(compute_prob(hunts_counter))
    
    return (max(prob))