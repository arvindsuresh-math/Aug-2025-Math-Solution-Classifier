def solve():
    """Index: 572.
    Returns: the number of pounds of lingonberries Steve had to pick on Thursday.
    """
    # L1
    pounds_monday = 8 # On Monday he picked 8 pounds
    pay_per_pound = 2 # The job paid $2 for every pound of lingonberries picked
    earnings_monday = pounds_monday * pay_per_pound

    # L2
    tuesday_multiplier = 3 # Tuesday’s harvest was triple what he had picked the previous day
    pounds_tuesday = tuesday_multiplier * pounds_monday

    # L3
    earnings_tuesday = pounds_tuesday * pay_per_pound

    # L4
    earnings_first_two_days = earnings_monday + earnings_tuesday

    # L5
    earnings_wednesday = 0 # rested on Wednesday
    total_earnings_before_thursday = earnings_first_two_days + earnings_wednesday

    # L6
    target_earnings = 100 # make a total of $100
    remaining_needed_earnings = target_earnings - total_earnings_before_thursday

    # L7
    pounds_thursday = remaining_needed_earnings / pay_per_pound

    # FA
    answer = pounds_thursday
    return answer