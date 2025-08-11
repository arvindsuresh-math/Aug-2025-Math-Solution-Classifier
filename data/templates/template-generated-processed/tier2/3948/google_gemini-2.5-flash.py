def solve():
    """Index: 3948.
    Returns: John's new combined total lifting capacity.
    """
    # L1
    initial_clean_jerk_weight = 80 # Clean & Jerk 80 kg
    double_factor = 2 # double his clean and jerk
    new_clean_jerk_weight = initial_clean_jerk_weight * double_factor

    # L2
    initial_snatch_weight = 50 # Snatch 50 kg
    snatch_increase_percent_decimal = 0.8 # increase his snatch by 80%
    snatch_increase_amount = initial_snatch_weight * snatch_increase_percent_decimal

    # L3
    new_snatch_weight = initial_snatch_weight + snatch_increase_amount

    # L4
    combined_total_lifting_capacity = new_clean_jerk_weight + new_snatch_weight

    # FA
    answer = combined_total_lifting_capacity
    return answer