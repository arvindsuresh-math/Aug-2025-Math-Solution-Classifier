from fractions import Fraction

def solve():
    """Index: 4174.
    Returns: the total pounds of coal all boxcars combined can hold.
    """
    # L2
    black_boxcar_capacity = 4000 # black boxcars can each hold 4000 pounds of coal
    half_factor = Fraction(1, 2) # half as much as what the blue boxcars can hold
    blue_boxcar_capacity = black_boxcar_capacity / half_factor

    # L3
    red_multiplier = 3 # red boxcars can hold 3 times as much as the blue boxcars
    red_boxcar_capacity = red_multiplier * blue_boxcar_capacity

    # L4
    num_red_boxcars = 3 # 3 red boxcars
    total_red_capacity = num_red_boxcars * red_boxcar_capacity

    # L5
    num_black_boxcars = 7 # 7 black boxcars
    total_black_capacity = num_black_boxcars * black_boxcar_capacity

    # L6
    num_blue_boxcars = 4 # 4 blue boxcars
    total_blue_capacity = num_blue_boxcars * blue_boxcar_capacity

    # L7
    total_combined_capacity = total_red_capacity + total_black_capacity + total_blue_capacity

    # FA
    answer = total_combined_capacity
    return answer