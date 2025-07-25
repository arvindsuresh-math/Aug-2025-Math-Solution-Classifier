def solve():
    """Index: 1138.
    Returns: the amount Jay will have saved at the end of four weeks.
    """
    # L1
    initial_savings = 20 # started by saving 20 dollars this week
    weekly_increase = 10 # increase the amount he saves each week by 10 dollars
    week1_savings = initial_savings + weekly_increase

    # L2
    week2_savings = week1_savings + weekly_increase

    # L3
    week3_savings = week2_savings + weekly_increase

    # L4
    week4_savings = week3_savings + weekly_increase

    # FA
    answer = week4_savings
    return answer