from fractions import Fraction

def solve():
    """Index: 4532.
    Returns: the total liters of water Mr. Reyansh uses for all his animals in a week.
    """
    # L1
    daily_cow_water_liters = 80 # Each cow on the farm drinks 80 liters of water daily
    days_per_week = 7 # WK
    weekly_cow_water_liters = daily_cow_water_liters * days_per_week

    # L2
    num_cows = 40 # 40 cows
    total_cow_water_weekly = weekly_cow_water_liters * num_cows

    # L3
    sheep_water_fraction = Fraction(1, 4) # 1/4 times as much water as a cow
    daily_sheep_water_liters = daily_cow_water_liters * sheep_water_fraction

    # L4
    weekly_sheep_water_liters = daily_sheep_water_liters * days_per_week

    # L5
    sheep_multiplier = 10 # 10 times the number of cows
    num_sheep = sheep_multiplier * num_cows

    # L6
    total_sheep_water_weekly = num_sheep * weekly_sheep_water_liters

    # L7
    total_water_per_week = total_sheep_water_weekly + total_cow_water_weekly

    # FA
    answer = total_water_per_week
    return answer