def solve():
    """Index: 665.
    Returns: the number of apples Bill has left.
    """
    # L1
    apples_per_child = 3 # 3 apples for their two favorite teachers
    num_children = 2 # two children
    apples_given_to_children = apples_per_child * num_children

    # L2
    num_pies = 2 # two apple pies
    apples_per_pie = 10 # 10 apples per pie
    apples_used_for_pies = apples_per_pie * num_pies

    # L3
    total_apples_used = apples_used_for_pies + apples_given_to_children

    # L4
    initial_apples = 50 # picked 50 apples
    apples_remaining = initial_apples - total_apples_used

    # FA
    answer = apples_remaining
    return answer