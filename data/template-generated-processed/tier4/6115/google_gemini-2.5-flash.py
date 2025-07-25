from fractions import Fraction

def solve():
    """Index: 6115.
    Returns: the total cost to make all the ice.
    """
    # L1
    pounds_needed = 10 # 10 pounds of cubes
    cube_weight_per_pound = Fraction(1, 16) # each cube weighs 1/16th of a pound
    total_cubes_needed = pounds_needed / cube_weight_per_pound

    # L2
    cubes_per_hour = 10 # 1 hour to make 10 cubes
    total_hours_needed = total_cubes_needed / cubes_per_hour

    # L3
    cost_per_hour_ice_maker = 1.50 # Every hour his ice maker run costs $1.50
    ice_maker_cost = total_hours_needed * cost_per_hour_ice_maker

    # L4
    ounces_per_cube = 2 # 2 ounces of water make 1 cube
    total_ounces_water_needed = total_cubes_needed * ounces_per_cube

    # L5
    cost_per_ounce_water = 0.10 # Every ounce of water costs $0.10
    water_cost = total_ounces_water_needed * cost_per_ounce_water

    # L6
    total_cost = ice_maker_cost + water_cost

    # FA
    answer = total_cost
    return answer