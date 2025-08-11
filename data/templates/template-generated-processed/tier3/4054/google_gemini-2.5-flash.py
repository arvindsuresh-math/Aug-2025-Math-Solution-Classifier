def solve():
    """Index: 4054.
    Returns: the amount John paid for the lawyer.
    """
    # L1
    court_hours = 50 # 50 hours in court time
    prep_time_multiplier = 2 # 2 times that long in prep time
    prep_hours = court_hours * prep_time_multiplier

    # L2
    total_hours = prep_hours + court_hours

    # L3
    hourly_rate = 100 # $100 per hour
    hourly_cost = total_hours * hourly_rate

    # L4
    upfront_cost = 1000 # $1000 upfront
    total_fee_before_brother = hourly_cost + upfront_cost

    # L5
    brother_share_divisor = 2 # His brother pays half the fee
    johns_payment = total_fee_before_brother / brother_share_divisor

    # FA
    answer = johns_payment
    return answer