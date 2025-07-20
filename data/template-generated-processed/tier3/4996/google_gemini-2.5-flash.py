def solve():
    """Index: 4996.
    Returns: the number of bottles of soda Rebecca will have left.
    """
    # L1
    packs_bought = 3 # three 6-packs of sodas
    bottles_per_pack = 6 # 6-packs of sodas
    total_bottles_bought = packs_bought * bottles_per_pack

    # L2
    num_weeks = 4 # four weeks
    days_per_week = 7 # A week is 7 days
    total_half_bottles_drunk = num_weeks * days_per_week

    # L3
    half_bottles_per_bottle = 2 # A bottle is two half bottles
    total_bottles_drunk = total_half_bottles_drunk / half_bottles_per_bottle

    # L4
    bottles_left = total_bottles_bought - total_bottles_drunk

    # FA
    answer = bottles_left
    return answer