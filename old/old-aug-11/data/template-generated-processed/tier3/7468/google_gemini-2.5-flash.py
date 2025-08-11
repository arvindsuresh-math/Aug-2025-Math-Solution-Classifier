def solve():
    """Index: 7468.
    Returns: the distance from Elise's house to the hospital in miles.
    """
    # L1
    total_paid = 23 # paid a total of $23
    base_price = 3 # a base price of $3
    cost_for_distance = total_paid - base_price

    # L2
    cost_per_mile = 4 # $4 for every mile she traveled
    distance_miles = cost_for_distance / cost_per_mile

    # FA
    answer = distance_miles
    return answer