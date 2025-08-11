def solve():
    """Index: 2460.
    Returns: the total pay Jenna gets for a round trip.
    """
    # L1
    one_way_miles = 400 # drives 400 miles one way
    num_ways = 2 # round trip (2 ways)
    total_miles = one_way_miles * num_ways

    # L2
    pay_per_mile = 0.40 # paid $0.40 per mile
    total_pay = total_miles * pay_per_mile

    # FA
    answer = total_pay
    return answer