def solve():
    """Index: 1138.
    Returns: the amount Jay will have saved in the fourth week from now.
    """
    # L1
    initial_saving = 20 # started by saving 20 dollars this week
    weekly_increase = 10 # increase the amount he saves each week by 10 dollars
    saving_week_1_from_now = initial_saving + weekly_increase

    # L2
    saving_week_2_from_now = saving_week_1_from_now + weekly_increase

    # L3
    saving_week_3_from_now = saving_week_2_from_now + weekly_increase

    # L4
    saving_week_4_from_now = saving_week_3_from_now + weekly_increase

    # FA
    answer = saving_week_4_from_now
    return answer