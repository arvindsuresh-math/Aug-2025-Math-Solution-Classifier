def solve():
    """Index: 2336.
    Returns: the number of additional hours Latia has to work to buy the TV.
    """
    # L1
    work_hours_per_week = 30 # 30-hour workweek
    hourly_wage = 10 # $10 per hour
    weekly_earnings = work_hours_per_week * hourly_wage

    # L2
    weeks_per_month = 4 # WK
    monthly_earnings = weekly_earnings * weeks_per_month

    # L3
    tv_cost = 1700 # Samsung TV worth $1700
    remaining_amount_needed = tv_cost - monthly_earnings

    # L4
    additional_hours_needed = remaining_amount_needed / hourly_wage

    # FA
    answer = additional_hours_needed
    return answer