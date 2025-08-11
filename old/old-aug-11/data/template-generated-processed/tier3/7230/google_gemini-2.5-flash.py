from fractions import Fraction

def solve():
    """Index: 7230.
    Returns: the total number of scoops Mitch needs.
    """
    # L1
    flour_cups = 3 # 3 cups of flour
    scoop_size = Fraction(1, 3) # a 1/3 cup scoop
    flour_scoops = flour_cups / scoop_size

    # L2
    sugar_cups = 2 # two cups of sugar
    sugar_scoops = sugar_cups / scoop_size

    # L3
    total_scoops = flour_scoops + sugar_scoops

    # FA
    answer = total_scoops
    return answer