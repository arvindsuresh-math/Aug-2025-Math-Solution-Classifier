def solve():
    """Index: 269.
    Returns: the amount of money John still needs to earn.
    """
    # L1
    saturday_earnings = 18 # John earned $18 on Saturday
    half_divisor = 2 # half that amount
    sunday_earnings = saturday_earnings / half_divisor

    # L2
    previous_weekend_earnings = 20 # He earned $20 the previous weekend
    total_earnings = saturday_earnings + sunday_earnings + previous_weekend_earnings

    # L3
    pogo_stick_cost = 60 # $60 he needs to buy a new pogo stick
    money_needed = pogo_stick_cost - total_earnings

    # FA
    answer = money_needed
    return answer