from fractions import Fraction

def solve():
    """Index: 400.
    Returns: the total weight Karen is carrying after six hours.
    """
    # L1
    water_loss_per_hour = 2 # drinks 2 pounds of water per hour
    food_fraction_of_water = Fraction(1, 3) # eats 1/3rd the weight of food per hour as water per hour
    food_loss_per_hour = water_loss_per_hour * food_fraction_of_water

    # L2
    total_loss_per_hour = water_loss_per_hour + food_loss_per_hour

    # L3
    hike_duration_hours = 6 # after six hours
    total_weight_lost = total_loss_per_hour * hike_duration_hours

    # L4
    water_packed = 20 # packs 20 pounds of water
    food_packed = 10 # 10 pounds of food
    gear_packed = 20 # 20 pounds of gear
    initial_total_weight = water_packed + food_packed + gear_packed

    # L5
    final_weight = initial_total_weight - total_weight_lost

    # FA
    answer = final_weight
    return answer