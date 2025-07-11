def solve():
    """Index: 2683.
    Returns: the total number of magazines Alexandra has now.
    """
    # L1
    magazines_friday = 8 # bought 8 magazines at the bookstore on Friday
    magazines_saturday = 12 # bought 12 more [on Saturday]
    magazines_friday_saturday = magazines_saturday + magazines_friday

    # L2
    multiplier_sunday = 4 # four times the number of magazines she did on Friday
    magazines_sunday = magazines_friday * multiplier_sunday

    # L3
    total_before_dog = magazines_saturday + magazines_friday + magazines_sunday

    # L4
    chewed_magazines = 4 # her dog had chewed up 4 of the magazines
    final_magazines = total_before_dog - chewed_magazines

    # FA
    answer = final_magazines
    return answer