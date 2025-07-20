def solve():
    """Index: 3763.
    Returns: the number of apple pies remaining with Cooper.
    """
    # L1
    pies_per_day = 7 # 7 apple pies a day
    num_days = 12 # for 12 days
    total_pies_made = pies_per_day * num_days

    # L2
    ashley_eats = 50 # eats 50 of his pies
    remaining_pies = total_pies_made - ashley_eats

    # FA
    answer = remaining_pies
    return answer