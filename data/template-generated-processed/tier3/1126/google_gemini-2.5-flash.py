def solve():
    """Index: 1126.
    Returns: the number of bricks of other types Mike is going to use.
    """
    # L1
    bricks_type_A = 40 # at least 40 bricks of type A
    half_divisor = 2 # half that many
    bricks_type_B = bricks_type_A / half_divisor

    # L2
    total_bricks_A_B = bricks_type_A + bricks_type_B

    # L3
    total_bricks_needed = 150 # In total, he needs to use 150 bricks
    other_types_bricks = total_bricks_needed - total_bricks_A_B

    # FA
    answer = other_types_bricks
    return answer