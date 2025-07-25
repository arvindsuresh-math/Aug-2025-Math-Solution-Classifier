def solve():
    """Index: 5890.
    Returns: the total miles Laura drives per week.
    """
    # L1
    school_round_trip_miles = 20 # Laura’s House is a 20-mile round trip from her school.
    days_per_week = 7 # WK
    miles_to_school_per_week = days_per_week * school_round_trip_miles

    # L2
    school_one_way_distance = school_round_trip_miles / 2 # Derived from school_round_trip_miles
    supermarket_additional_distance = 10 # 10 miles farther away from the school
    supermarket_one_way_miles = school_one_way_distance + supermarket_additional_distance

    # L3
    round_trip_multiplier = 2 # WK
    supermarket_round_trip_miles = supermarket_one_way_miles * round_trip_multiplier

    # L4
    supermarket_trips_per_week = 2 # two afternoons a week drives to the supermarket
    miles_to_supermarket_per_week = supermarket_round_trip_miles * supermarket_trips_per_week

    # L5
    total_miles_per_week = miles_to_school_per_week + miles_to_supermarket_per_week

    # FA
    answer = total_miles_per_week
    return answer