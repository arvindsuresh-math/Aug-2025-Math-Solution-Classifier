def solve():
    """Index: 5423.
    Returns: the total miles John skateboarded.
    """
    # L1
    skateboarded_to_park = 10 # skateboarded for 10 miles
    walked_to_park = 4 # walked another 4 miles
    total_to_park = skateboarded_to_park + walked_to_park

    # L2
    round_trip_multiplier = 2 # WK
    total_round_trip = total_to_park * round_trip_multiplier

    # L3
    total_skateboarded = total_round_trip - walked_to_park

    # FA
    answer = total_skateboarded
    return answer