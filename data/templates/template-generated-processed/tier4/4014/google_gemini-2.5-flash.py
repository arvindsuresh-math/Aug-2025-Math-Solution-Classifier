from fractions import Fraction

def solve():
    """Index: 4014.
    Returns: the percentage of hot sauce in the bottle.
    """
    # L1
    daily_shampoo_usage = 1 # 1 oz of shampoo a day
    daily_hot_sauce_replacement = Fraction(1, 2) # 1/2 an ounce of hot sauce
    daily_net_decrease = daily_shampoo_usage - daily_hot_sauce_replacement

    # L2
    num_days = 4 # After 4 days
    total_decrease_ounces = num_days * daily_net_decrease

    # L3
    initial_bottle_volume = 10 # new 10 oz bottle
    remaining_liquid_volume = initial_bottle_volume - total_decrease_ounces

    # L4
    total_hot_sauce_volume = num_days * daily_hot_sauce_replacement

    # L5
    proportion_hot_sauce = total_hot_sauce_volume / remaining_liquid_volume

    # L6
    percentage_multiplier = 100 # WK
    final_percentage_hot_sauce = proportion_hot_sauce * percentage_multiplier

    # FA
    answer = final_percentage_hot_sauce
    return answer