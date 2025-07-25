def solve():
    """Index: 908.
    Returns: the total money John makes from the telethon.
    """
    # L1
    first_hours = 12 # first 12 hours
    base_rate = 5000 # $5000 per hour
    first_period_total = first_hours * base_rate

    # L2
    percent_increase = 0.2 # 20% more per hour
    extra_per_hour = base_rate * percent_increase

    # L3
    increased_rate = base_rate + extra_per_hour

    # L4
    second_hours = 14 # remaining 14 hours
    second_period_total = increased_rate * second_hours

    # L5
    total_money = second_period_total + first_period_total

    # FA
    answer = total_money
    return answer