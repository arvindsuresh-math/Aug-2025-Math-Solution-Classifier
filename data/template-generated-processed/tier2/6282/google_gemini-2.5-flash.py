def solve():
    """Index: 6282.
    Returns: the minimum amount it rained on the fourth day.
    """
    # L1
    rain_day1 = 10 # The first day it rained 10 inches
    twice_factor = 2 # rained twice that much
    rain_day2 = rain_day1 * twice_factor

    # L2
    fifty_percent_more_factor = 1.5 # rained 50% more than the second day
    rain_day3 = rain_day2 * fifty_percent_more_factor

    # L3
    total_rain_first_3_days = rain_day1 + rain_day2 + rain_day3

    # L4
    total_storm_days = 4 # lasting 4 days
    drain_start_delay = 1 # flooded the fourth day before getting a chance to do any of the draining
    drain_days = total_storm_days - drain_start_delay

    # L5
    drain_rate_per_day = 3 # drain out the equivalent of 3 inches of rain per day
    total_drained_amount = drain_days * drain_rate_per_day

    # L6
    water_at_start_of_day4 = total_rain_first_3_days - total_drained_amount

    # L7
    capacity_feet = 6 # can hold the equivalent of 6 feet of rain
    inches_per_foot = 12 # WK
    capacity_inches = capacity_feet * inches_per_foot

    # L8
    min_rain_day4 = capacity_inches - water_at_start_of_day4

    # FA
    answer = min_rain_day4
    return answer