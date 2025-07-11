def solve():
    """Index: 1876.
    Returns: the number of additional gift bags Carl needs to make.
    """
    # L1
    known_attendees = 50 # 50 people will show up
    hoped_attendees = 40 # another 40 people will randomly show up
    total_expected_people = known_attendees + hoped_attendees

    # L2
    extravagant_bags = 10 # 10 extravagant gift bags
    average_bags = 20 # average gift bags for 20 people
    total_bags_made = extravagant_bags + average_bags

    # L3
    bags_needed = total_expected_people - total_bags_made

    # FA
    answer = bags_needed
    return answer