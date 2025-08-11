from fractions import Fraction

def solve():
    """Index: 5562.
    Returns: the number of potatoes Marcel bought.
    """
    # L1
    marcel_corn = 10 # Marcel buys 10 ears of corn
    dale_corn_fraction = Fraction(1, 2) # half that amount
    dale_corn_denominator = 2 # 1/2 what Marcel did
    dale_corn = marcel_corn * dale_corn_fraction

    # L2
    total_corn = marcel_corn + dale_corn

    # L4
    total_vegetables = 27 # end up buying 27 vegetables
    total_potatoes = total_vegetables - total_corn

    # L5
    dale_potatoes = 8 # Dale buys 8 potatoes
    marcel_potatoes = total_potatoes - dale_potatoes

    # FA
    answer = marcel_potatoes
    return answer