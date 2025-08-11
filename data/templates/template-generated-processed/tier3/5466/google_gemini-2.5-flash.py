from fractions import Fraction

def solve():
    """Index: 5466.
    Returns: the total number of cubes Gage has.
    """
    # L1
    red_fraction_given = Fraction(2, 5) # 2/5 of his red numbered cubes
    grady_red_cubes = 20 # 20 red numbered cubes
    red_cubes_given_by_grady = red_fraction_given * grady_red_cubes

    # L2
    gage_initial_red_cubes = 10 # 10 red numbered cubes
    gage_total_red_cubes = gage_initial_red_cubes + red_cubes_given_by_grady

    # L3
    blue_fraction_given = Fraction(1, 3) # 1/3 of the blue numbered cubes
    grady_blue_cubes = 15 # 15 blue numbered cubes
    blue_cubes_given_by_grady = blue_fraction_given * grady_blue_cubes

    # L4
    gage_initial_blue_cubes = 12 # 12 blue numbered cubes
    gage_total_blue_cubes = gage_initial_blue_cubes + blue_cubes_given_by_grady

    # L5
    gage_total_cubes = gage_total_blue_cubes + gage_total_red_cubes

    # FA
    answer = gage_total_cubes
    return answer