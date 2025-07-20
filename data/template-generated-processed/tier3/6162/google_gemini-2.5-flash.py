from fractions import Fraction

def solve():
    """Index: 6162.
    Returns: the cost of erasers.
    """
    # L1
    pencils_sold = 20 # sold 20 pencils
    erasers_per_pencil = 2 # for every pencil you buy, you must buy 2 erasers
    erasers_sold = pencils_sold * erasers_per_pencil

    # L4
    total_earned = 80 # earned $80
    eraser_price_ratio = Fraction(1, 2) # cost 1/2 the price of the pencils
    effective_units_for_pencil_price = pencils_sold + (eraser_price_ratio * erasers_sold)
    pencil_price = total_earned / effective_units_for_pencil_price

    # L5
    eraser_price_denominator = 2 # 1/2 the price of the pencils
    eraser_cost = pencil_price / eraser_price_denominator

    # FA
    answer = eraser_cost
    return answer