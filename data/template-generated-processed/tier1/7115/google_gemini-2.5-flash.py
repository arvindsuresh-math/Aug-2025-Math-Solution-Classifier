def solve():
    """Index: 7115.
    Returns: the percentage of mornings Jake does not drop his coffee.
    """
    # L1
    trips_percent_val = 40 # Jake trips over his dog 40% percent of mornings
    drops_if_trips_percent_val = 25 # 25% of the time he trips
    trips_and_drops_coffee_percent_val = (trips_percent_val / 100) * (drops_if_trips_percent_val / 100) * 100

    # L2
    total_percent_val = 100 # WK
    not_drop_coffee_percent_val = total_percent_val - trips_and_drops_coffee_percent_val

    # FA
    answer = not_drop_coffee_percent_val
    return answer