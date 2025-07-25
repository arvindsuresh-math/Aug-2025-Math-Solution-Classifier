def solve():
    """Index: 6884.
    Returns: the total number of pockets Janet's dresses have.
    """
    # L1
    total_dresses = 24 # Janet has 24 dresses
    half_divisor = 2 # Half of them
    dresses_with_pockets = total_dresses / half_divisor

    # L2
    third_divisor = 3 # a third have 2 pockets
    pockets_per_dress_two = 2 # have 2 pockets
    dresses_with_two_pockets = dresses_with_pockets / third_divisor

    # L3
    pockets_per_dress_three = 3 # the rest have 3 pockets
    dresses_with_three_pockets = dresses_with_pockets - dresses_with_two_pockets

    # L4
    total_pockets_from_two_pocket_dresses = pockets_per_dress_two * dresses_with_two_pockets

    # L5
    total_pockets_from_three_pocket_dresses = dresses_with_three_pockets * pockets_per_dress_three

    # L6
    total_pockets = total_pockets_from_two_pocket_dresses + total_pockets_from_three_pocket_dresses

    # FA
    answer = total_pockets
    return answer