from fractions import Fraction

def solve():
    """Index: 2220.
    Returns: the total amount of time, in minutes, Luke and Paula take traveling each day.
    """
    # L1
    luke_bus_time_to_work = 70 # Luke takes a 70-minute bus to work
    paula_time_fraction_numerator = 3 # 3/5 of this time
    paula_time_fraction_denominator = 5 # 3/5 of this time
    paula_bus_time_to_work = Fraction(paula_time_fraction_numerator, paula_time_fraction_denominator) * luke_bus_time_to_work

    # L2
    paula_total_daily_travel_time = paula_bus_time_to_work + paula_bus_time_to_work

    # L3
    luke_bike_speed_factor = 5 # 5 times slower than the bus
    luke_bike_time_from_work = luke_bike_speed_factor * luke_bus_time_to_work

    # L4
    luke_total_daily_travel_time = luke_bike_time_from_work + luke_bus_time_to_work

    # L5
    total_travel_time = luke_total_daily_travel_time + paula_total_daily_travel_time

    # FA
    answer = total_travel_time
    return answer