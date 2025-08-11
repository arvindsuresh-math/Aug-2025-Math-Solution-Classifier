def solve():
    """Index: 2228.
    Returns: the total pounds of oats needed for 3 days.
    """
    # L1
    num_horses = 4 # four horses
    oats_per_horse_per_feeding = 4 # 4 pounds of oats
    pounds_per_feeding = num_horses * oats_per_horse_per_feeding

    # L2
    feedings_per_day = 2 # twice a day
    pounds_per_day = pounds_per_feeding * feedings_per_day

    # L3
    num_days = 3 # for 3 days
    total_oats_needed = pounds_per_day * num_days

    # FA
    answer = total_oats_needed
    return answer