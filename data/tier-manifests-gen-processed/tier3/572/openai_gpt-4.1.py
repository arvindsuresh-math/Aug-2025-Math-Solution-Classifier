def solve():
    """Index: 572.
    Returns: the number of pounds Steve had to pick on Thursday.
    """
    # L1
    monday_pounds = 8 # On Monday he picked 8 pounds
    pay_per_pound = 2 # paid $2 for every pound
    monday_earnings = monday_pounds * pay_per_pound

    # L2
    tuesday_multiplier = 3 # Tuesday’s harvest was triple what he had picked the previous day
    tuesday_pounds = tuesday_multiplier * monday_pounds

    # L3
    tuesday_earnings = tuesday_pounds * pay_per_pound

    # L4
    first_two_days_earnings = monday_earnings + tuesday_earnings

    # L5
    wednesday_earnings = 0 # Wednesday he felt very tired and decided to rest
    total_earnings = first_two_days_earnings + wednesday_earnings

    # L6
    target_earnings = 100 # Steve wanted to make a total of $100
    earnings_difference = target_earnings - total_earnings

    # L7
    thursday_pounds = earnings_difference / pay_per_pound

    # FA
    answer = thursday_pounds
    return answer