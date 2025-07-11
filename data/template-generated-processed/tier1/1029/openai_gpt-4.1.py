def solve():
    """Index: 1029.
    Returns: the total number of pails of milk Farmer Red gets from his three cows each week.
    """
    # L1
    bess_daily = 2 # Bess gives him two pails of milk every day

    # L2
    brownie_multiplier = 3 # Brownie produces three times that amount
    brownie_daily = brownie_multiplier * bess_daily

    # L3
    daisy_more_than_bess = 1 # Daisy makes one pail more than Bess
    daisy_daily = bess_daily + daisy_more_than_bess

    # L4
    total_daily = bess_daily + brownie_daily + daisy_daily

    # L5
    days_in_week = 7 # WK
    total_weekly = total_daily * days_in_week

    # FA
    answer = total_weekly
    return answer