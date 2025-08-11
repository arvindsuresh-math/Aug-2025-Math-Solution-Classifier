def solve():
    """Index: 6714.
    Returns: the maximum amount Paul could receive from his dad.
    """
    # L1
    reward_b_plus_initial = 5 # $5 for every B+
    doubling_factor = 2 # double the previous rewards
    reward_b_plus_doubled = doubling_factor * reward_b_plus_initial

    # L2
    twice_factor = 2 # twice that amount for every A
    reward_a_initial = reward_b_plus_initial * twice_factor

    # L3
    reward_a_doubled = doubling_factor * reward_a_initial

    # L5
    num_a_plus_for_bonus = 2 # at least two A+
    total_courses = 10 # 10 courses
    reward_a_plus_flat = 15 # $15 for every A+ obtained
    remaining_courses_for_a = total_courses - num_a_plus_for_bonus

    # L7
    payout_a_plus_part = num_a_plus_for_bonus * reward_a_plus_flat
    payout_a_part = remaining_courses_for_a * reward_a_doubled
    total_payout = payout_a_plus_part + payout_a_part

    # FA
    answer = total_payout
    return answer