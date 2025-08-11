def solve():
    """Index: 3175.
    Returns: the total cost of cable for the neighborhood.
    """
    # L1
    num_ew_streets = 18 # 18 east-west streets
    len_ew_street = 2 # 2 miles long
    total_ew_distance = num_ew_streets * len_ew_street

    # L2
    num_ns_streets = 10 # 10 north-south streets
    len_ns_street = 4 # four miles long
    total_ns_distance = num_ns_streets * len_ns_street

    # L3
    total_street_distance = total_ew_distance + total_ns_distance

    # L4
    cable_per_street_mile = 5 # 5 miles of cable to electrify 1 mile of street
    total_cable_miles = total_street_distance * cable_per_street_mile

    # L5
    cost_per_mile = 2000 # $2000/mile
    total_cost = total_cable_miles * cost_per_mile

    # FA
    answer = total_cost
    return answer