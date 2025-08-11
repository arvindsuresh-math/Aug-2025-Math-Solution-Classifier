from fractions import Fraction

def solve():
    """Index: 6946.
    Returns: the number of supplies remaining in the ship.
    """
    # L1
    initial_food_supply = 400 # 400 pounds of food for the journey's supply
    first_day_fraction_used = Fraction(2, 5) # 2/5 of the supplies had been used
    food_used_first_day = first_day_fraction_used * initial_food_supply

    # L2
    remaining_supplies_after_first_day = initial_food_supply - food_used_first_day

    # L3
    subsequent_days_fraction_used = Fraction(3, 5) # 3/5 of the remaining supplies
    food_used_subsequent_days = subsequent_days_fraction_used * remaining_supplies_after_first_day

    # L4
    final_remaining_supplies = remaining_supplies_after_first_day - food_used_subsequent_days

    # FA
    answer = final_remaining_supplies
    return answer