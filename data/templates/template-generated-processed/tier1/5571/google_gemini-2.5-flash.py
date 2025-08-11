def solve():
    """Index: 5571.
    Returns: the total weight of the hotdogs that Mason ate.
    """
    # L1
    noah_burgers_eaten = 8 # If Noah ate 8 burgers
    jacob_fewer_pies = 3 # Jacob eats three fewer pies than Noah eats burgers
    jacob_pies_eaten = noah_burgers_eaten - jacob_fewer_pies

    # L2
    mason_times_pies = 3 # Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob
    mason_hotdogs_eaten = jacob_pies_eaten * mason_times_pies

    # L3
    hotdog_weight = 2 # A hot dog weighs 2 ounces
    total_hotdog_weight = mason_hotdogs_eaten * hotdog_weight

    # FA
    answer = total_hotdog_weight
    return answer