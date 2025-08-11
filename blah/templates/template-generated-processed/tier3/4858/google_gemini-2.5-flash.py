from fractions import Fraction

def solve():
    """Index: 4858.
    Returns: the total money collected from selling the fruits at the new prices.
    """
    # L1
    lemon_initial_price = 8 # planned to sell the lemons at $8
    lemon_price_increase = 4 # price of lemons had risen by $4
    lemon_new_price = lemon_initial_price + lemon_price_increase

    # L2
    num_lemons = 80 # 80 lemons
    total_lemon_revenue = lemon_new_price * num_lemons

    # L3
    grape_increase_fraction = Fraction(1, 2) # half the price
    grape_price_increase = grape_increase_fraction * lemon_price_increase

    # L4
    grape_initial_price = 7 # the grapes at $7
    grape_new_price = grape_initial_price + grape_price_increase

    # L5
    num_grapes = 140 # 140 grapes
    total_grape_revenue = num_grapes * grape_new_price

    # L6
    total_revenue = total_grape_revenue + total_lemon_revenue

    # FA
    answer = total_revenue
    return answer