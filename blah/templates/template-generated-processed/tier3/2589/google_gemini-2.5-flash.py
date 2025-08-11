def solve():
    """Index: 2589.
    Returns: the number of adults in Bob's family.
    """
    # L1
    num_children = 33 # 33 children in his family
    apples_per_child = 10 # each of them ate 10 apples
    apples_eaten_by_children = num_children * apples_per_child

    # L2
    total_apples = 450 # Bob picked 450 apples
    apples_left_for_adults = total_apples - apples_eaten_by_children

    # L3
    apples_per_adult = 3 # every adult ate 3 apples apiece
    num_adults = apples_left_for_adults / apples_per_adult

    # FA
    answer = num_adults
    return answer