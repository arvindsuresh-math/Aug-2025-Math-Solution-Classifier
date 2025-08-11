from fractions import Fraction

def solve():
    """Index: 5478.
    Returns: the number of liters of water collected on the third day.
    """
    # L1
    tank_capacity = 100 # A tank can hold 100 liters of water
    initial_fill_fraction = Fraction(2, 5) # the tank is 2/5 filled with water
    initial_water_volume = tank_capacity * initial_fill_fraction

    # L2
    first_day_collected = 15 # collected 15 liters of water
    water_after_day1 = initial_water_volume + first_day_collected

    # L3
    additional_on_day2 = 5 # 5 liters more water was collected than on the first day
    second_day_collected = first_day_collected + additional_on_day2

    # L4
    water_after_day2 = water_after_day1 + second_day_collected

    # L5
    third_day_collected = tank_capacity - water_after_day2

    # FA
    answer = third_day_collected
    return answer