def solve():
    """Index: 2395.
    Returns: the total number of guests served by the chef.
    """
    # L1
    adults = 58 # 58 adults
    fewer_children = 35 # 35 fewer children than the number of adults
    children = adults - fewer_children

    # L2
    seniors_per_child = 2 # twice as many seniors as children
    seniors = children * seniors_per_child

    # L3
    total_guests = adults + children + seniors

    # FA
    answer = total_guests
    return answer