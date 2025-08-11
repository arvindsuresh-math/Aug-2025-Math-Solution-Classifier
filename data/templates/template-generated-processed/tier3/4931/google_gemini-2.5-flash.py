from fractions import Fraction

def solve():
    """Index: 4931.
    Returns: the number of dandelions that survive long enough to flower.
    """
    # L1
    initial_seeds = 300 # Each dandelion produces 300 seeds
    water_fraction = Fraction(1, 3) # 1/3rd of the seeds
    seeds_in_water = initial_seeds * water_fraction

    # L2
    eaten_fraction = Fraction(1, 6) # 1/6 of the starting number
    seeds_eaten = initial_seeds * eaten_fraction

    # L3
    remaining_seeds_before_sprouting = initial_seeds - seeds_in_water - seeds_eaten

    # L4
    sprout_divisor = 2 # Half the remainder sprout
    surviving_dandelions = remaining_seeds_before_sprouting / sprout_divisor

    # FA
    answer = surviving_dandelions
    return answer