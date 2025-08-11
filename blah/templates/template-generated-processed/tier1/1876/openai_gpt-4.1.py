def solve():
    """Index: 1876.
    Returns: the number of additional gift bags Carl needs to make.
    """
    # L1
    known_guests = 50 # knows 50 people will show up
    hoped_guests = 40 # hopes that another 40 people will randomly show up
    total_guests = known_guests + hoped_guests

    # L2
    extravagant_bags = 10 # created 10 extravagant gift bags
    average_bags = 20 # made average gift bags for 20 people
    total_bags_made = extravagant_bags + average_bags

    # L3
    bags_needed = total_guests - total_bags_made

    # FA
    answer = bags_needed
    return answer