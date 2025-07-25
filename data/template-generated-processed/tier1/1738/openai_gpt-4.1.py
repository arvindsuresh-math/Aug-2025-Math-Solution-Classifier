def solve():
    """Index: 1738.
    Returns: how many more apple pies Steve bakes than cherry pies in one week.
    """
    # L1
    apple_pie_days = 3 # Mondays, Wednesdays and Fridays
    pies_per_day = 12 # he bakes 12 pies per day
    apple_pies_per_week = apple_pie_days * pies_per_day

    # L2
    cherry_pie_days = 2 # Tuesdays and Thursdays
    cherry_pies_per_week = cherry_pie_days * pies_per_day

    # L3
    more_apple_pies = apple_pies_per_week - cherry_pies_per_week

    # FA
    answer = more_apple_pies
    return answer