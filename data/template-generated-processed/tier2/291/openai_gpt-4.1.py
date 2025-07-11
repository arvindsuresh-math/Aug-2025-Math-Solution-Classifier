def solve():
    """Index: 291.
    Returns: the total fuel Mary used in the two weeks.
    """
    # L1
    this_week_fuel = 15 # Mary used 15 gallons of fuel this week
    percent_less = 0.2 # 20% less
    fuel_less = this_week_fuel * percent_less

    # L2
    last_week_fuel = this_week_fuel - fuel_less

    # L3
    total_fuel = this_week_fuel + last_week_fuel

    # FA
    answer = total_fuel
    return answer