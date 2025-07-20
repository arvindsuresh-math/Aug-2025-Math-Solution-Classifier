def solve():
    """Index: 4641.
    Returns: the number of children at the basketball match.
    """
    # L1
    total_spectators = 10000 # 10000 spectators
    men_spectators = 7000 # 7000 of them were men
    women_and_children = total_spectators - men_spectators

    # L2
    children_multiplier = 5 # 5 times as many children as women
    women_ratio_part = 1 # WK
    num_women = women_and_children / (children_multiplier + women_ratio_part)

    # L3
    num_children = num_women * children_multiplier

    # FA
    answer = num_children
    return answer