def solve():
    """Index: 6192.
    Returns: the number of apples Mom will have left over.
    """
    # L1
    total_apples_to_split = 18 # 18 apples
    num_children_splitting = 2 # split evenly
    apples_per_child = total_apples_to_split / num_children_splitting

    # L2
    susan_multiplier = 2 # twice as many apples as Greg
    susan_apples = susan_multiplier * apples_per_child

    # L3
    mark_fewer_apples = 5 # 5 fewer apples than Susan
    mark_apples = susan_apples - mark_fewer_apples

    # L4
    total_children_apples = apples_per_child + apples_per_child + susan_apples + mark_apples

    # L5
    mom_needs_apples = 40 # needs 40 apples
    apples_left_over = total_children_apples - mom_needs_apples

    # FA
    answer = apples_left_over
    return answer