def solve():
    """Index: 4704.
    Returns: the total time John spends on the trip.
    """
    # L1
    first_country_weeks = 2 # stays in the first country for 2 weeks
    multiplier_twice = 2 # twice as long
    weeks_per_other_country = first_country_weeks * multiplier_twice

    # L2
    num_other_countries = 2 # each of the other two countries
    total_weeks_other_countries = num_other_countries * weeks_per_other_country

    # L3
    total_trip_weeks = first_country_weeks + total_weeks_other_countries

    # FA
    answer = total_trip_weeks
    return answer