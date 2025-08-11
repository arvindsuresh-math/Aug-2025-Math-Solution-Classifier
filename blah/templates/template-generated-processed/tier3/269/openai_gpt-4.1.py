def solve():
    """Index: 269.
    Returns: the extra amount John needs to buy the pogo stick.
    """
    # L1
    saturday_earnings = 18 # John earned $18 on Saturday
    sunday_divisor = 2 # half that amount on Sunday
    sunday_earnings = saturday_earnings / sunday_divisor

    # L2
    previous_weekend_earnings = 20 # He earned $20 the previous weekend
    total_earnings = saturday_earnings + sunday_earnings + previous_weekend_earnings

    # L3
    pogo_stick_cost = 60 # $60 he needs to buy a new pogo stick
    extra_needed = pogo_stick_cost - total_earnings

    # FA
    answer = extra_needed
    return answer