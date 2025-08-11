from fractions import Fraction

def solve():
    """Index: 5327.
    Returns: the total price a buyer would pay for two pieces of jewelry and five paintings.
    """
    # L1
    initial_jewelry_price = 30 # jewelry at $30 each
    jewelry_price_increase = 10 # increase the price of jewelry by $10 each
    new_jewelry_price = initial_jewelry_price + jewelry_price_increase

    # L2
    painting_increase_percentage = Fraction(20, 100) # cost of each painting by 20%
    initial_painting_price = 100 # paintings at $100 each
    painting_price_increase_amount = painting_increase_percentage * initial_painting_price

    # L3
    new_painting_price = initial_painting_price + painting_price_increase_amount

    # L4
    num_jewelry_pieces = 2 # two pieces of jewelry
    total_cost_jewelry = num_jewelry_pieces * new_jewelry_price

    # L5
    num_paintings = 5 # five paintings
    total_cost_paintings = new_painting_price * num_paintings

    # L6
    final_total_cost = total_cost_paintings + total_cost_jewelry

    # FA
    answer = final_total_cost
    return answer