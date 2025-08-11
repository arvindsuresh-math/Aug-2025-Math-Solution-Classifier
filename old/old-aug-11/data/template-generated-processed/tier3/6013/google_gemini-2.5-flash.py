def solve():
    """Index: 6013.
    Returns: the amount of a 20% tip.
    """
    # L1
    tip_amount_15_percent = 42 # 15% tip of $42
    percentage_known = 15 # If 15% is known
    percentage_part = 5 # then 5% can be found
    division_factor = percentage_known / percentage_part
    tip_amount_5_percent = tip_amount_15_percent / division_factor

    # L2
    target_percentage = 20 # 20% tip
    tip_amount_20_percent = tip_amount_5_percent + tip_amount_15_percent

    # FA
    answer = tip_amount_20_percent
    return answer