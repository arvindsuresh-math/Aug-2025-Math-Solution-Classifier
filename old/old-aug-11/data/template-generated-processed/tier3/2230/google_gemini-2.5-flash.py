def solve():
    """Index: 2230.
    Returns: the number of weeks Alfonso needs to work to buy his mountain bike.
    """
    # L1
    helmet_cost = 340 # mountain bike helmet for $340
    current_savings = 40 # he already has $40
    remaining_amount_needed = helmet_cost - current_savings

    # L2
    daily_earnings = 6 # $6 each day
    days_worked_per_week = 5 # walks his aunt's dog 5 days a week
    weekly_earnings = daily_earnings * days_worked_per_week

    # L3
    weeks_to_work = remaining_amount_needed / weekly_earnings

    # FA
    answer = weeks_to_work
    return answer