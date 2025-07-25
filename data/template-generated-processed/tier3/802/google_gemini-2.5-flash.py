from fractions import Fraction

def solve():
    """Index: 802.
    Returns: the number of birds Ivan's bird feeder feeds weekly.
    """
    # L1
    total_capacity = 2 # holds two cups of birdseed
    squirrel_theft = Fraction(1, 2) # steals half a cup of birdseed
    actual_birdseed_eaten = total_capacity - squirrel_theft

    # L2
    birds_per_cup = 14 # Each cup of birdseed can feed fourteen birds
    total_birds_fed = birds_per_cup * actual_birdseed_eaten

    # FA
    answer = total_birds_fed
    return answer