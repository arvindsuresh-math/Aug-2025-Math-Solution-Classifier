def solve():
    """Index: 3438.
    Returns: the total money Penn made after 5 days.
    """
    # L1
    first_day_earnings = 10 # On the first day, she made $10
    daily_increase = 4 # made $4 more than the previous day
    second_day_earnings = first_day_earnings + daily_increase

    # L2
    third_day_earnings = second_day_earnings + daily_increase

    # L3
    fourth_day_earnings = third_day_earnings + daily_increase

    # L4
    fifth_day_earnings = fourth_day_earnings + daily_increase

    # L5
    total_earnings = first_day_earnings + second_day_earnings + third_day_earnings + fourth_day_earnings + fifth_day_earnings

    # FA
    answer = total_earnings
    return answer