def solve():
    """Index: 5169.
    Returns: the total money earned by the amusement park in a week.
    """
    # L1
    people_per_weekday = 100 # 100 people per day
    weekdays_in_week = 5 # WK
    total_weekday_visitors = people_per_weekday * weekdays_in_week

    # L2
    saturday_visitors = 200 # on Saturday it was visited by 200 people
    sunday_visitors = 300 # on Sunday by 300
    total_weekend_visitors = saturday_visitors + sunday_visitors

    # L3
    total_weekly_visitors = total_weekday_visitors + total_weekend_visitors

    # L4
    ticket_price = 3 # tickets for $3
    total_money_earned = total_weekly_visitors * ticket_price

    # FA
    answer = total_money_earned
    return answer