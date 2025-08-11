def solve():
    """Index: 4452.
    Returns: the number of Dodge trucks in the parking lot.
    """
    # L1
    num_vw_bugs = 5 # 5 Volkswagon Bugs
    multiplier_for_toyota = 2 # half as many Volkswagen Bugs as there are Toyota trucks
    num_toyota_trucks = multiplier_for_toyota * num_vw_bugs

    # L2
    multiplier_for_ford = 2 # twice as many Ford trucks as Toyota trucks
    num_ford_trucks = multiplier_for_ford * num_toyota_trucks

    # L3
    multiplier_for_dodge = 3 # one-third as many Ford trucks as Dodge trucks
    num_dodge_trucks = num_ford_trucks * multiplier_for_dodge

    # FA
    answer = num_dodge_trucks
    return answer