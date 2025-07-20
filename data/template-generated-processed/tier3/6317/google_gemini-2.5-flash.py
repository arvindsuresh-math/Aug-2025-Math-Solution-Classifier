def solve():
    """Index: 6317.
    Returns: the average amount of hours Brady worked per month.
    """
    # L1
    hours_per_day_april = 6 # worked 6 hours every day in April
    days_in_april = 30 # WK
    hours_april = hours_per_day_april * days_in_april

    # L2
    hours_per_day_june = 5 # worked 5 hours every day in June
    days_in_june = 30 # WK
    hours_june = hours_per_day_june * days_in_june

    # L3
    hours_per_day_september = 8 # worked 8 hours every day in September
    days_in_september = 30 # WK
    hours_september = hours_per_day_september * days_in_september

    # L4
    total_hours = hours_april + hours_june + hours_september

    # L5
    number_of_months = 3 # in those 3 months
    average_hours_per_month = total_hours / number_of_months

    # FA
    answer = average_hours_per_month
    return answer