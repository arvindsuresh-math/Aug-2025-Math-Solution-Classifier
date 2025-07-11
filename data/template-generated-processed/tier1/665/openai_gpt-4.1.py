def solve():
    """Index: 665.
    Returns: the number of apples Bill has left after giving apples to his kids and his wife baking pies.
    """
    # L1
    apples_per_child = 3 # sends each of his kids to school with 3 apples
    num_children = 2 # his wife and two children -> two children
    apples_given_to_kids = apples_per_child * num_children

    # L2
    apples_per_pie = 10 # using 10 apples per pie
    num_pies = 2 # bakes two apple pies
    apples_used_for_pies = apples_per_pie * num_pies

    # L3
    total_apples_used = apples_used_for_pies + apples_given_to_kids

    # L4
    initial_apples = 50 # Bill picked 50 apples
    apples_remaining = initial_apples - total_apples_used

    # FA
    answer = apples_remaining
    return answer