def solve():
    """Index: 5084.
    Returns: the total amount of money she makes from good and tough weeks.
    """
    # L1
    tough_week_sales = 800 # sells goods worth $800
    half_multiplier = 2 # half the amount she sells on a good week
    good_week_sales = tough_week_sales * half_multiplier

    # L2
    num_good_weeks = 5 # 5 good weeks
    total_good_weeks_sales = num_good_weeks * good_week_sales

    # L3
    num_tough_weeks = 3 # 3 tough weeks
    total_tough_weeks_sales = num_tough_weeks * tough_week_sales

    # L4
    total_sales = total_tough_weeks_sales + total_good_weeks_sales

    # FA
    answer = total_sales
    return answer