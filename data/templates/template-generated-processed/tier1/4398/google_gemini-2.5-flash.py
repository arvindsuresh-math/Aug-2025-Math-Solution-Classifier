def solve():
    """Index: 4398.
    Returns: the total pounds of bamboo the pandas will eat in a week.
    """
    # L1
    adult_panda_daily_eat = 138 # 138 pounds of bamboo each day
    days_in_week = 7 # WK
    adult_panda_weekly_eat = adult_panda_daily_eat * days_in_week

    # L2
    baby_panda_daily_eat = 50 # 50 pounds of bamboo a day
    baby_panda_weekly_eat = baby_panda_daily_eat * days_in_week

    # L3
    total_weekly_eat = adult_panda_weekly_eat + baby_panda_weekly_eat

    # FA
    answer = total_weekly_eat
    return answer