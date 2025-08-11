from fractions import Fraction

def solve():
    """Index: 4730.
    Returns: the total number of animals remaining on the farm.
    """
    # L1
    num_cows = 184 # 184 cows
    cows_to_dogs_ratio = 2 # twice as many cows as dogs
    initial_dogs = num_cows / cows_to_dogs_ratio

    # L2
    cows_sold_fraction = Fraction(1, 4) # sell 1/4 of the cows
    cows_sold = cows_sold_fraction * num_cows

    # L3
    remaining_cows = num_cows - cows_sold

    # L4
    dogs_sold_fraction = Fraction(3, 4) # 3/4 of the dogs
    dogs_sold = dogs_sold_fraction * initial_dogs

    # L5
    remaining_dogs = initial_dogs - dogs_sold

    # L6
    total_remaining_animals = remaining_dogs + remaining_cows

    # FA
    answer = total_remaining_animals
    return answer