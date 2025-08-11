def solve():
    """Index: 908.
    Returns: the total money John makes from the telethon.
    """
    # L1
    first_period_hours = 12 # For the first 12 hours
    rate_first_period = 5000 # generates $5000 per hour
    money_first_period = first_period_hours * rate_first_period

    # L2
    increase_percent_decimal = 0.2 # generates 20% more per hour
    increase_amount_per_hour = rate_first_period * increase_percent_decimal

    # L3
    rate_second_period = rate_first_period + increase_amount_per_hour

    # L4
    second_period_hours = 14 # remaining 14 hours
    money_second_period = rate_second_period * second_period_hours

    # L5
    total_money = money_second_period + money_first_period

    # FA
    answer = total_money
    return answer