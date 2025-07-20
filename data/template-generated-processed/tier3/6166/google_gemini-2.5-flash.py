from fractions import Fraction

def solve():
    """Index: 6166.
    Returns: the total number of strawberries each hedgehog ate.
    """
    # L1
    num_baskets = 3 # three baskets
    strawberries_per_basket = 900 # each with 900 strawberries
    total_initial_strawberries = num_baskets * strawberries_per_basket

    # L2
    remaining_fraction = Fraction(2, 9) # 2/9 of the strawberries were remaining
    strawberries_remaining = remaining_fraction * total_initial_strawberries

    # L3
    strawberries_eaten_total = total_initial_strawberries - strawberries_remaining

    # L4
    num_hedgehogs = 2 # Two hedgehogs
    strawberries_eaten_per_hedgehog = strawberries_eaten_total / num_hedgehogs

    # FA
    answer = strawberries_eaten_per_hedgehog
    return answer