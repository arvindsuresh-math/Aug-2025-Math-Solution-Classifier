from fractions import Fraction

def solve():
    """Index: 3847.
    Returns: the number of nice people in the crowd.
    """
    # L1
    num_barry = 24 # 24 people named Barry
    barry_nice_fraction = 1 # All people named Barry are nice
    nice_barry = barry_nice_fraction * num_barry

    # L2
    num_kevin = 20 # 20 people named Kevin
    kevin_nice_fraction = 0.5 # half of the people named Kevin are nice
    nice_kevin = kevin_nice_fraction * num_kevin

    # L3
    num_julie = 80 # 80 people named Julie
    julie_nice_fraction = Fraction(3, 4) # Three-fourths of people named Julie are nice
    nice_julie = julie_nice_fraction * num_julie

    # L4
    num_joe = 50 # 50 people named Joe
    joe_nice_fraction = 0.1 # 10% of people named Joe are nice
    nice_joe = joe_nice_fraction * num_joe

    # L5
    total_nice_people = nice_barry + nice_kevin + nice_julie + nice_joe

    # FA
    answer = total_nice_people
    return answer