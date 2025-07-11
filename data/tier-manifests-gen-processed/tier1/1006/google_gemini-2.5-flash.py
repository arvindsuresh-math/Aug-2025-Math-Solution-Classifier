def solve():
    """Index: 1006.
    Returns: Jayson's mom's age when he was born.
    """
    # L1
    jayson_age_at_time_1 = 10 # When Jayson is 10
    dad_age_multiplier = 4 # four times his age
    dad_age_at_time_1 = jayson_age_at_time_1 * dad_age_multiplier

    # L2
    mom_age_difference_from_dad = 2 # 2 years younger than his dad
    mom_age_at_time_1 = dad_age_at_time_1 - mom_age_difference_from_dad

    # L3
    mom_age_at_birth = mom_age_at_time_1 - jayson_age_at_time_1

    # FA
    answer = mom_age_at_birth
    return answer