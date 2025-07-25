def solve():
    """Index: 291.
    Returns: the total fuel used for the two weeks.
    """
    # L1
    current_week_fuel_gallons = 15 # 15 gallons of fuel this week
    less_percent_decimal = 0.2 # 20% less
    fuel_less_last_week = current_week_fuel_gallons * less_percent_decimal

    # L2
    last_week_fuel_gallons = current_week_fuel_gallons - fuel_less_last_week

    # L3
    total_fuel_gallons = current_week_fuel_gallons + last_week_fuel_gallons

    # FA
    answer = total_fuel_gallons
    return answer