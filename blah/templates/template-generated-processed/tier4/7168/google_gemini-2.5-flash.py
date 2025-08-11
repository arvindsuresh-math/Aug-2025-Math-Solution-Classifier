def solve():
    """Index: 7168.
    Returns: the number of missed field goals that went wide right.
    """
    # L1
    total_attempts = 60 # He attempts 60 field goals
    missed_divisor = 4 # He misses 1/4 of the field goals
    missed_field_goals = total_attempts / missed_divisor

    # L2
    wide_right_decimal = 0.20 # 20 percent were wide right
    wide_right_missed_field_goals = missed_field_goals * wide_right_decimal

    # FA
    answer = wide_right_missed_field_goals
    return answer