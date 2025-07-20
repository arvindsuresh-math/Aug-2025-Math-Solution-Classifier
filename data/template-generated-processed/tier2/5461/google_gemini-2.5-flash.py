def solve():
    """Index: 5461.
    Returns: the total number of cents June earns.
    """
    # L1
    total_clovers = 200 # June picks 200 clovers in total
    three_petal_percentage_decimal = 0.75 # 75% have 3 petals
    clovers_3_petals = total_clovers * three_petal_percentage_decimal

    # L2
    two_petal_percentage_decimal = 0.24 # 24% have two petals
    clovers_2_petals = total_clovers * two_petal_percentage_decimal

    # L3
    four_petal_percentage_decimal = 0.01 # 1% have four petals
    clovers_4_petals = total_clovers * four_petal_percentage_decimal

    # L4
    petals_per_3_leaf_clover = 3 # WK
    value_3_petal_clovers = clovers_3_petals * petals_per_3_leaf_clover

    # L5
    petals_per_2_leaf_clover = 2 # WK
    value_2_petal_clovers = clovers_2_petals * petals_per_2_leaf_clover

    # L6
    multiplier_for_4_leaf_clover_value = 2 # WK
    value_4_petal_clovers = clovers_4_petals * multiplier_for_4_leaf_clover_value

    # L7
    total_cents = value_3_petal_clovers + value_2_petal_clovers + value_4_petal_clovers

    # FA
    answer = total_cents
    return answer