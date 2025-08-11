def solve():
    """Index: 2996.
    Returns: the total gallons of gas the car will consume.
    """
    # L1
    gallons_per_mile = 4 # consumes 4 gallons of gas per mile
    miles_today = 400 # drives 400 miles today
    gallons_consumed_today = gallons_per_mile * miles_today

    # L2
    more_miles_tomorrow = 200 # 200 more miles tomorrow
    miles_tomorrow = more_miles_tomorrow + miles_today

    # L3
    gallons_consumed_tomorrow = gallons_per_mile * miles_tomorrow

    # L4
    total_gallons_consumed = gallons_consumed_tomorrow + gallons_consumed_today

    # FA
    answer = total_gallons_consumed
    return answer