def solve():
    """Index: 5752.
    Returns: the total number of people in the group.
    """
    # L1
    women_per_child_multiplier = 3 # number of women is 3 times the number of children
    children_count = 30 # number of children is 30
    women_count = women_per_child_multiplier * children_count

    # L2
    men_per_woman_multiplier = 2 # number of men is twice the number of women
    men_count = men_per_woman_multiplier * women_count

    # L3
    total_people = men_count + women_count + children_count

    # FA
    answer = total_people
    return answer