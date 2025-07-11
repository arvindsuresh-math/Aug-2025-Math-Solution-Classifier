def solve():
    """Index: 1690.
    Returns: how many more centimeters it rained on Tuesdays than Mondays.
    """
    # L1
    num_mondays = 7 # On each of 7 Mondays
    rain_per_monday = 1.5 # it rained 1.5 centimeters
    total_monday_rain = num_mondays * rain_per_monday

    # L2
    num_tuesdays = 9 # On each of 9 Tuesdays
    rain_per_tuesday = 2.5 # it rained 2.5 centimeters
    total_tuesday_rain = num_tuesdays * rain_per_tuesday

    # L3
    rain_difference = total_tuesday_rain - total_monday_rain

    # FA
    answer = rain_difference
    return answer