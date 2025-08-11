def solve():
    """Index: 5952.
    Returns: the total weight gained by the three family members.
    """
    # L1
    orlando_gain = 5 # Orlando gained 5 pounds
    twice_multiplier = 2 # twice what Orlando gained
    twice_orlando_gain = twice_multiplier * orlando_gain

    # L2
    jose_additional_gain = 2 # two pounds more
    jose_gain = jose_additional_gain + twice_orlando_gain

    # L3
    half_divisor = 2 # Half of what Jose gained
    half_jose_gain = jose_gain / half_divisor

    # L4
    fernando_less_gain = 3 # 3 pounds less
    fernando_gain = half_jose_gain - fernando_less_gain

    # L5
    total_gain = orlando_gain + jose_gain + fernando_gain

    # FA
    answer = total_gain
    return answer