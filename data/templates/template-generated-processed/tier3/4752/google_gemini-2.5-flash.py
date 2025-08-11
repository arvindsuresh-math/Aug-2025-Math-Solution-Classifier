def solve():
    """Index: 4752.
    Returns: the difference in percentage points between the percentage of nails painted blue and striped.
    """
    # L1
    total_nails = 20 # 20 toenails and fingernails
    purple_nails = 6 # 6 of her nails purple
    blue_nails = 8 # 8 of them blue
    striped_nails = total_nails - purple_nails - blue_nails

    # L2
    percentage_multiplier = 100 # multiply by 100%
    blue_percentage = (blue_nails / total_nails) * percentage_multiplier

    # L3
    striped_percentage = (striped_nails / total_nails) * percentage_multiplier

    # L4
    percentage_difference = blue_percentage - striped_percentage

    # FA
    answer = percentage_difference
    return answer