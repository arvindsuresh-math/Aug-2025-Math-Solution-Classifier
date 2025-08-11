def solve():
    """Index: 1738.
    Returns: the number of more apple pies baked than cherry pies in one week.
    """
    # L1
    days_apple_pie = 3 # On Mondays, Wednesdays and Fridays
    pies_per_day = 12 # 12 pies per day
    total_apple_pies = days_apple_pie * pies_per_day

    # L2
    days_cherry_pie = 2 # On Tuesdays and Thursdays
    total_cherry_pies = days_cherry_pie * pies_per_day

    # L3
    difference_pies = total_apple_pies - total_cherry_pies

    # FA
    answer = difference_pies
    return answer