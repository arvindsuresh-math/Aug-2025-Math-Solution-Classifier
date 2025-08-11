from fractions import Fraction

def solve():
    """Index: 811.
    Returns: the total number of fish Steve has in stock.
    """
    # L1
    initial_stock = 200 # stock of 200 fish
    sold_fish = 50 # sells 50 fish
    remaining_after_sale = initial_stock - sold_fish

    # L2
    spoiled_fraction = Fraction(1, 3) # a third of the remaining fish
    spoiled_fish = spoiled_fraction * remaining_after_sale

    # L3
    remaining_after_spoilage = remaining_after_sale - spoiled_fish

    # L4
    new_stock = 200 # A new stock of 200 more fish arrives
    total_current_stock = remaining_after_spoilage + new_stock

    # FA
    answer = total_current_stock
    return answer