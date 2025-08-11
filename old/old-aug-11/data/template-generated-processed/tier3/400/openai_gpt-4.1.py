from fractions import Fraction

def solve():
    """Index: 400.
    Returns: the weight Karen is carrying after six hours of hiking.
    """
    # L1
    water_per_hour = 2 # drinks 2 pounds of water per hour
    food_fraction = Fraction(1, 3) # eats 1/3rd the weight of food per hour as water per hour
    food_per_hour = water_per_hour * food_fraction

    # L2
    total_loss_per_hour = water_per_hour + food_per_hour

    # L3
    hours_hiked = 6 # after six hours
    total_weight_lost = total_loss_per_hour * hours_hiked

    # L4
    water_start = 20 # 20 pounds of water
    food_start = 10 # 10 pounds of food
    gear_start = 20 # 20 pounds of gear
    starting_weight = water_start + food_start + gear_start

    # L5
    weight_after_hiking = starting_weight - total_weight_lost

    # FA
    answer = weight_after_hiking
    return answer