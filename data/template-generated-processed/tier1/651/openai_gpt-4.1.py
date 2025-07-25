def solve():
    """Index: 651.
    Returns: the total amount of money Olivia made this week.
    """
    # L1
    hourly_wage = 9 # earns $9 per hour
    hours_monday = 4 # worked 4 hours on Monday
    monday_earnings = hourly_wage * hours_monday

    # L2
    hours_wednesday = 3 # worked 3 hours on Wednesday
    wednesday_earnings = hourly_wage * hours_wednesday

    # L3
    hours_friday = 6 # worked 6 hours on Friday
    friday_earnings = hourly_wage * hours_friday

    # L4
    total_earnings = monday_earnings + wednesday_earnings + friday_earnings

    # FA
    answer = total_earnings
    return answer