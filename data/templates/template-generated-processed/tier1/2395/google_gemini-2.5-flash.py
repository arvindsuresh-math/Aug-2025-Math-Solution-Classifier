def solve():
    """Index: 2395.
    Returns: the total number of guests served.
    """
    # L1
    adults_served = 58 # 58 adults
    children_fewer_than_adults = 35 # 35 fewer children than the number of adults
    children_served = adults_served - children_fewer_than_adults

    # L2
    seniors_multiplier_children = 2 # twice as many seniors as children
    seniors_served = children_served * seniors_multiplier_children

    # L3
    total_guests = adults_served + children_served + seniors_served

    # FA
    answer = total_guests
    return answer