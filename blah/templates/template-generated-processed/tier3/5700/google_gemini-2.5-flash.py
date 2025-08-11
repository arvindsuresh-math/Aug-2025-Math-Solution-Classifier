def solve():
    """Index: 5700.
    Returns: the number of snack eaters left.
    """
    # L1
    total_participants = 200 # 200 people participating
    initial_snack_calculation_subtrahend = 100 # 200-100
    initial_snack_eaters = total_participants - initial_snack_calculation_subtrahend

    # L2
    new_outsiders_joined_first = 20 # 20 new outsiders joined in to have a snack
    current_snack_eaters_after_first_join = initial_snack_eaters + new_outsiders_joined_first

    # L3
    half_divisor_first_departure = 2 # Half of these snack eaters got full and left
    snack_eaters_left_after_first_departure = current_snack_eaters_after_first_join / half_divisor_first_departure

    # L4
    new_outsiders_joined_second = 10 # 10 new outsiders came to have snacks, too
    current_snack_eaters_after_second_join = snack_eaters_left_after_first_departure + new_outsiders_joined_second

    # L5
    snack_eaters_left_second = 30 # 30 more snack eaters got their fill and left
    snack_eaters_after_second_departure = current_snack_eaters_after_second_join - snack_eaters_left_second

    # L6
    half_divisor_final_departure = 2 # half of the remaining snack eaters left later on
    final_snack_eaters = snack_eaters_after_second_departure / half_divisor_final_departure

    # FA
    answer = final_snack_eaters
    return answer