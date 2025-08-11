def solve():
    """Index: 6001.
    Returns: Berry's average temperature for the week.
    """
    # L1
    sunday_temp = 99.1 # On Sunday his temperature is 99.1
    monday_temp = 98.2 # On Monday his temperature is 98.2
    tuesday_temp = 98.7 # On Tuesday his temperature is 98.7
    wednesday_temp = 99.3 # On Wednesday his temperature is 99.3
    thursday_temp = 99.8 # On Thursday his temperature is 99.8
    friday_temp = 99.0 # On Friday his temperature is 99
    saturday_temp = 98.9 # On Saturday his temperature is 98.9
    total_temperature_stated_L1 = 692 # He total temperature for the week is 692

    # L2
    total_temperature_for_average = 693 # 693 divided by 7
    num_days_in_week = 7 # WK
    average_temperature = total_temperature_for_average / num_days_in_week

    # FA
    answer = average_temperature
    return answer