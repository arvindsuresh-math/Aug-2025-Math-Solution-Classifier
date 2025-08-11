def solve():
    """Index: 2460.
    Returns: the total pay Jenna gets for a round trip.
    """
    # L1
    miles_one_way = 400 # drives 400 miles one way
    num_ways = 2 # for a round trip
    total_miles = miles_one_way * num_ways

    # L2
    pay_per_mile = 0.40 # gets paid $0.40 cents per mile
    total_pay = total_miles * pay_per_mile

    # FA
    answer = total_pay
    return answer