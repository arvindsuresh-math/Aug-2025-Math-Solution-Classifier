def solve():
    """Index: 2996.
    Returns: the total gallons of gas Dream's car will consume in two days.
    """
    # L1
    gas_per_mile = 4 # car consumes 4 gallons of gas per mile
    miles_today = 400 # drives 400 miles today
    gas_today = gas_per_mile * miles_today

    # L2
    more_miles_tomorrow = 200 # 200 more miles tomorrow than today
    miles_tomorrow = more_miles_tomorrow + miles_today

    # L3
    gas_tomorrow = gas_per_mile * miles_tomorrow

    # L4
    total_gas = gas_tomorrow + gas_today

    # FA
    answer = total_gas
    return answer