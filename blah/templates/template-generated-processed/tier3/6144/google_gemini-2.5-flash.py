def solve():
    """Index: 6144.
    Returns: the number of kids still awake.
    """
    # L1
    total_kids = 20 # 20 kids in preschool
    first_half_divisor = 2 # 1/2 of the kids
    kids_asleep_first_round = total_kids / first_half_divisor

    # L2
    kids_awake_after_first_round = total_kids - kids_asleep_first_round

    # L3
    second_half_divisor = 2 # half of the kids remaining
    kids_still_awake = kids_awake_after_first_round / second_half_divisor

    # FA
    answer = kids_still_awake
    return answer