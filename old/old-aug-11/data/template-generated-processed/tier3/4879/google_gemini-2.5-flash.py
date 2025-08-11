def solve():
    """Index: 4879.
    Returns: the difference in the number of limbs between five aliens and five Martians.
    """
    # L1
    alien_arms = 3 # Aliens have three arms
    martian_arm_multiplier = 2 # twice as many arms
    martian_arms_per_martian = martian_arm_multiplier * alien_arms

    # L2
    alien_legs = 8 # eight legs
    martian_leg_divisor = 2 # half as many legs
    martian_legs_per_martian = alien_legs / martian_leg_divisor

    # L3
    num_martians = 5 # five Martians
    num_martians_times_martian_arms = num_martians * martian_arms_per_martian
    num_martians_times_martian_legs = num_martians * martian_legs_per_martian
    total_martian_limbs = num_martians_times_martian_arms + num_martians_times_martian_legs

    # L4
    num_aliens = 5 # five aliens
    num_aliens_times_alien_arms = num_aliens * alien_arms
    num_aliens_times_alien_legs = num_aliens * alien_legs
    total_alien_limbs = num_aliens_times_alien_arms + num_aliens_times_alien_legs

    # L5
    limbs_difference = total_alien_limbs - total_martian_limbs

    # FA
    answer = limbs_difference
    return answer