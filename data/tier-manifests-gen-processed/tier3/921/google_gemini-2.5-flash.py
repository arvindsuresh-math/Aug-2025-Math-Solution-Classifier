from fractions import Fraction

def solve():
    """Index: 921.
    Returns: the total number of recyclable cans and bottles collected.
    """
    # L1
    total_people = 90 # There were 90 people at the summer picnic
    soda_drank_fraction_denominator = 2 # One-half of the guests drank soda
    soda_drinkers = total_people / soda_drank_fraction_denominator

    # L2
    sparkling_water_drank_fraction_denominator = 3 # one-third of the guests drank sparkling water
    sparkling_water_drinkers = total_people / sparkling_water_drank_fraction_denominator

    # L3
    juice_consumed_fraction = Fraction(4, 5) # four-fifths of the juices were consumed
    total_juice_bottles = 50 # 50 glass bottles of juice
    juice_consumed = juice_consumed_fraction * total_juice_bottles

    # L4
    total_recyclables = soda_drinkers + sparkling_water_drinkers + juice_consumed

    # FA
    answer = total_recyclables
    return answer