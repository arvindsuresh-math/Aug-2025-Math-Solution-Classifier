def solve():
    """Index: 5910.
    Returns: the remaining ounces of coffee after being shrink zapped.
    """
    # L1
    num_cups = 5 # 5 cups
    ounces_per_cup = 8 # 8 ounces of fluid
    total_ounces_before_zap = num_cups * ounces_per_cup

    # L2
    shrink_factor = 0.5 # shrink by 50%
    total_ounces_after_zap = shrink_factor * total_ounces_before_zap

    # FA
    answer = total_ounces_after_zap
    return answer