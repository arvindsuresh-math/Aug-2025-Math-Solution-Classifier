def solve():
    """Index: 3119.
    Returns: the total space all cans take up after being compacted.
    """
    # L1
    num_cans = 60 # 60 cans
    space_per_can_before_compact = 30 # 30 square inches of space before being compacted
    total_space_before_compact = num_cans * space_per_can_before_compact

    # L2
    compacted_percentage_num = 20 # 20% of that amount
    percent_factor = 0.01 # WK
    total_space_after_compact = total_space_before_compact * compacted_percentage_num * percent_factor

    # FA
    answer = total_space_after_compact
    return answer