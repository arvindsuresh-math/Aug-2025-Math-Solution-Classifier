def solve():
    """Index: 1817.
    Returns: the number of pumps needed to fill all the tires.
    """
    # L1
    tire_capacity = 500 # Each tire can hold 500 cubic inches of air
    num_empty_tires = 2 # Two of the tires are completely flat and empty
    empty_tires_air_needed = tire_capacity * num_empty_tires

    # L3
    tire_40_full_percent = 40 # One tire is 40% full
    percent_100 = 100 # WK
    percent_factor = 0.01 # WK
    tire_40_needed_percent = percent_100 - tire_40_full_percent
    tire_40_air_needed = tire_capacity * (tire_40_needed_percent * percent_factor)

    # L5
    tire_70_full_percent = 70 # last tire is 70% full
    tire_70_needed_percent = percent_100 - tire_70_full_percent
    tire_70_air_needed = tire_capacity * (tire_70_needed_percent * percent_factor)

    # L6
    total_air_needed = empty_tires_air_needed + tire_40_air_needed + tire_70_air_needed

    # L7
    pump_capacity = 50 # Carson injects 50 cubic inches of air with each pump
    pumps_needed = total_air_needed / pump_capacity

    # FA
    answer = pumps_needed
    return answer